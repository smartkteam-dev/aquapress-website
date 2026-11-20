(function(){
  var nav=document.getElementById('main-nav');
  var sentinel=document.getElementById('top-sentinel');
  if(nav&&sentinel&&'IntersectionObserver' in window){
    new IntersectionObserver(function(e){nav.classList.toggle('scrolled',!e[0].isIntersecting)}).observe(sentinel);
  }
  var hamBtn=document.getElementById('ham-btn'),mobileMenu=document.getElementById('mobile-menu');
  if(hamBtn&&mobileMenu){
    var focusables=function(){return [hamBtn].concat([].slice.call(mobileMenu.querySelectorAll('a[href],button')))};
    var setOpen=function(open,restoreFocus){
      mobileMenu.classList.toggle('open',open);
      hamBtn.setAttribute('aria-expanded',open?'true':'false');
      hamBtn.setAttribute('aria-label',open?'Cerrar menú':'Abrir menú');
      document.body.style.overflow=open?'hidden':'';
      if(open){var first=mobileMenu.querySelector('a[href]');if(first)first.focus()}
      else if(restoreFocus){hamBtn.focus()}
    };
    hamBtn.addEventListener('click',function(){setOpen(!mobileMenu.classList.contains('open'))});
    [].slice.call(mobileMenu.querySelectorAll('.mobile-link,.btn')).forEach(function(el){el.addEventListener('click',function(){setOpen(false)})});
    document.addEventListener('keydown',function(e){
      if(!mobileMenu.classList.contains('open'))return;
      if(e.key==='Escape'){setOpen(false,true);return}
      if(e.key!=='Tab')return;
      var f=focusables(),i=f.indexOf(document.activeElement);
      if(e.shiftKey&&i<=0){e.preventDefault();f[f.length-1].focus()}
      else if(!e.shiftKey&&i===f.length-1){e.preventDefault();f[0].focus()}
    });
  }
  // Google Analytics click events (the Google tag itself is GTAG_HTML in tools/lib.py).
  // Mark whatsapp_click and phone_click as key events in GA4: they are this site's leads.
  document.addEventListener('click',function(e){
    var a=e.target&&e.target.closest?e.target.closest('a[href]'):null;
    if(!a||typeof window.gtag!=='function')return;
    var href=a.getAttribute('href')||'',name=null;
    if(/^https:\/\/(wa\.me|api\.whatsapp\.com)\//.test(href))name='whatsapp_click';
    else if(href.indexOf('tel:')===0)name='phone_click';
    else if(href.indexOf('mailto:')===0)name='email_click';
    else if(/^https:\/\/(maps\.app\.goo\.gl|(www\.)?google\.[a-z.]+\/maps)/.test(href))name='directions_click';
    if(name)window.gtag('event',name,{link_url:href,link_text:(a.textContent||a.getAttribute('aria-label')||'').trim().slice(0,80),page_path:location.pathname});
  });
  var items=document.querySelectorAll('.fade-up');
  if('IntersectionObserver' in window){
    var obs=new IntersectionObserver(function(entries){entries.forEach(function(e){if(e.isIntersecting){e.target.classList.add('visible');obs.unobserve(e.target)}})},{threshold:.1});
    items.forEach(function(el){obs.observe(el)});
  }else{
    items.forEach(function(el){el.classList.add('visible')});
  }
})();
