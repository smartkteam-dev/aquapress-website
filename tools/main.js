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
  var items=document.querySelectorAll('.fade-up');
  if('IntersectionObserver' in window){
    var obs=new IntersectionObserver(function(entries){entries.forEach(function(e){if(e.isIntersecting){e.target.classList.add('visible');obs.unobserve(e.target)}})},{threshold:.1});
    items.forEach(function(el){obs.observe(el)});
  }else{
    items.forEach(function(el){el.classList.add('visible')});
  }
})();
