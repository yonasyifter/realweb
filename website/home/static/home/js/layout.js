document.addEventListener('DOMContentLoaded',()=>{
  element = document.querySelector('.sidenav');
  M.Sidenav.init(element, {edge:'left', draggable:true, preventScrolling:true});
});
