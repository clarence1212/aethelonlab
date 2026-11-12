(function(){
  /* Pillar filter on the index */
  var bar = document.getElementById('filters');
  if (bar){
    var line = document.getElementById('pillarLine'), feat = document.getElementById('feat');
    var rows = Array.prototype.slice.call(document.querySelectorAll('[data-pillar]'));
    bar.addEventListener('click', function(e){
      var b = e.target.closest('button'); if (!b) return;
      var p = b.getAttribute('data-f');
      Array.prototype.forEach.call(bar.querySelectorAll('button'), function(x){ x.setAttribute('aria-pressed', x === b); });
      rows.forEach(function(r){ r.hidden = p !== 'all' && r.getAttribute('data-pillar') !== p; });
      if (feat) feat.hidden = p !== 'all' && p !== '1';
      line.textContent = b.getAttribute('data-line');
    });
  }
  /* Reading progress on a note */
  var prog = document.getElementById('prog');
  if (prog){
    var upd = function(){
      var h = document.documentElement, max = h.scrollHeight - h.clientHeight;
      prog.style.width = (max > 0 ? Math.min(100, h.scrollTop / max * 100) : 0) + '%';
    };
    document.addEventListener('scroll', upd, { passive: true }); upd();
  }
  /* Copy a note as rich text, for pasting into a newsletter editor */
  var copy = document.getElementById('copy');
  if (copy){
    copy.addEventListener('click', function(){
      var art = document.getElementById('art');
      var body = art.querySelector('.body').cloneNode(true);
      Array.prototype.forEach.call(body.querySelectorAll('figure'), function(f){ f.remove(); });
      var refs = art.querySelector('.refs');
      var html = '<h1>' + art.querySelector('h1').innerHTML + '</h1><p><em>' + art.querySelector('.dek').innerHTML + '</em></p>' +
        body.innerHTML + (refs ? '<h3>Further reading</h3><ul>' + refs.innerHTML + '</ul>' : '') +
        '<p><em>First published at <a href="' + copy.getAttribute('data-url') + '">aethelonlab.com</a>.</em></p>';
      var tmp = document.createElement('div'); tmp.innerHTML = html;
      var text = tmp.innerText || tmp.textContent;
      var done = function(ok){ copy.textContent = ok ? 'Copied' : 'Copy failed, select the text instead'; setTimeout(function(){ copy.textContent = 'Copy for newsletter'; }, 2600); };
      try {
        if (window.ClipboardItem && navigator.clipboard.write){
          navigator.clipboard.write([new ClipboardItem({ 'text/html': new Blob([html], { type: 'text/html' }), 'text/plain': new Blob([text], { type: 'text/plain' }) })])
            .then(function(){ done(true); }, function(){ navigator.clipboard.writeText(text).then(function(){ done(true); }, function(){ done(false); }); });
        } else { navigator.clipboard.writeText(text).then(function(){ done(true); }, function(){ done(false); }); }
      } catch (err){ done(false); }
    });
  }
})();
