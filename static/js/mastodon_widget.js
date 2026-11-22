/* Mastodon thread-reply widget (brothertown-language-com #32).
 *
 * Client-side enhancement for blog entry pages: locates the entry's
 * `View on Mastodon` anchor (the thread URL of record), parses the status id,
 * fetches the status's public context (replies) from the Mastodon API at view
 * time, and renders the replies as text beneath the Comment on Mastodon
 * section. Every failure path degrades silently to the exact current form.
 *
 * Security discipline: reply content is untrusted and is inserted ONLY as
 * text nodes — reply HTML bodies are converted to text via DOMParser
 * (which does not execute scripts). No API-derived string is ever assigned to
 * element HTML properties or inserted as markup.
 */
(function () {
  'use strict';

  var THREAD_RE = /:\/\/[^/]*mastodon\.social\/@([^/<]+)\/(\d+)/;
  var API_BASE = 'https://mastodon.social/api/v1/statuses/';
  var FETCH_TIMEOUT_MS = 8000;
  var CONTAINER_ID = 'mastodon-replies';

  function findThreadAnchor() {
    var anchors = document.querySelectorAll('a[href]');
    for (var i = 0; i < anchors.length; i++) {
      var m = THREAD_RE.exec(anchors[i].href);
      if (m && anchors[i].textContent.indexOf('View on Mastodon') !== -1) {
        return { anchor: anchors[i], statusId: m[2] };
      }
    }
    return null;
  }

  function findSection(anchor) {
    /* Walk up from the anchor looking for the `Comment on Mastodon` h3;
     * the h3 is no ancestor of the anchor in this markup, so this normally
     * returns null and the container inserts directly after the anchor —
     * beneath the section, which is what R-1 asks for. */
    var node = anchor;
    var heading = null;
    while (node && node !== document.body) {
      node = node.parentElement;
      if (!node) break;
      if (node.tagName === 'H3' &&
          node.textContent.indexOf('Comment on Mastodon') !== -1) {
        heading = node;
        break;
      }
    }
    return heading;
  }

  function makeText(tag, content, className) {
    var el = document.createElement(tag);
    if (className) { el.className = className; }
    el.textContent = content;
    return el;
  }

  function htmlToText(html) {
    /* DOMParser parses without executing scripts; we keep only text. */
    try {
      var doc = new DOMParser().parseFromString(html, 'text/html');
      return (doc.documentElement.textContent || '').trim();
    } catch (e) {
      return '';
    }
  }

  function renderReply(parent, reply) {
    var item = document.createElement('li');
    var acct = reply.account || {};
    var name = (acct.display_name || '').trim() || acct.username || 'unknown';
    var handle = acct.acct ? '@' + acct.acct : '';
    var when = '';
    if (reply.created_at) {
      var d = new Date(reply.created_at);
      if (!isNaN(d.getTime())) {
        when = d.toLocaleDateString(undefined, {
          year: 'numeric', month: 'long', day: 'numeric'
        });
      }
    }
    var who = handle ? name + ' (' + handle + ')' : name;
    if (when) { who += ' — ' + when; }
    item.appendChild(makeText('p', who, 'mastodon-reply-meta'));
    var body = htmlToText(reply.content || '');
    if (body) {
      item.appendChild(makeText('p', body, 'mastodon-reply-body'));
    }
    parent.appendChild(item);
  }

  function buildContainer() {
    var old = document.getElementById(CONTAINER_ID);
    if (old && old.parentElement) { old.parentElement.removeChild(old); }
    var div = document.createElement('div');
    div.id = CONTAINER_ID;
    return div;
  }

  function insertAfter(newNode, refNode) {
    if (refNode.parentElement) {
      refNode.parentElement.insertBefore(newNode, refNode.nextSibling);
      return true;
    }
    return false;
  }

  function main() {
    try {
      var found = findThreadAnchor();
      if (!found) { return; } /* not an entry page, or malformed anchor (KD-3) */
      var heading = findSection(found.anchor);
      var refNode = heading || found.anchor;
      fetch(API_BASE + found.statusId + '/context', {
        method: 'GET',
        signal: AbortSignal.timeout ? AbortSignal.timeout(FETCH_TIMEOUT_MS) : undefined,
        cache: 'default'
      }).then(function (resp) {
        if (!resp.ok) { return; } /* failure → silent (KD-3) */
        return resp.json();
      }).then(function (data) {
        try {
          if (!data || !Array.isArray(data.descendants)) { return; }
          var container = buildContainer();
          if (!insertAfter(container, refNode)) { return; }
          for (var i = 0; i < data.descendants.length; i++) {
            renderReply(container, data.descendants[i]);
          }
        } catch (e) { /* silent (KD-3) */ }
      }).catch(function () { /* silent (KD-3) */ });
    } catch (e) { /* silent (KD-3) */ }
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', main, { once: true });
  } else {
    main();
  }
})();
