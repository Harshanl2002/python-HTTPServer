const cor=document.querySelector(".planecards");
let isdragging=false
const draggstart=()=>{
    isdragging=true;
    cor.classList.add("dragging");
}
const dragging=(e)=>{
    if(!isdragging) return;
    cor.scrollLeft=e.pageX;
    console.log(e.pageX);
}
const dragstop=()=>{
    isdragging=true;
    cor.classList.remove("dragging");
}
cor.addEventListener("mousedown",draggstart);
cor.addEventListener("mousemove",dragging);
document.addEventListener("mouseup",dragstop);