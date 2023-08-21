//for nav scroll effect//
let height = screen.height
const navbar = document.querySelector(".navig")
const links = document.querySelector(".links")
const logoTxt = document.querySelector(".logoTxt")
window.onscroll = ()=> {
    this.scrollY > innerHeight ? navbar.classList.add("white") : navbar.classList.remove("white");
    this.scrollY > innerHeight ? links.classList.add("white") : links.classList.remove("white")
    this.scrollY > innerHeight ? logoTxt.classList.add("showTxt") : logoTxt.classList.remove("showTxt")
  }
//for gallery image effects//
const imgs = document.getElementsByClassName("galleryImg")
const backgroundHistoryImg = document.querySelector(".secMtn")
const histPage = document.querySelector(".secMtn")
const histContent = document.querySelector(".histContent")
const dots = document.getElementsByTagName("circle")

Array.from(imgs).forEach(img => {
    img.addEventListener('click',(e)=>{
        if(img.getAttribute("src")=="mtnGallery1.jpg"){
            backgroundHistoryImg.src = "mtnGallery1.jpg"
            histContent.style.backgroundColor = "aliceblue"
            histContent.style.opacity = 0.8
        }
        if (img.getAttribute("src")=="mtnGallery2.jpg" ){
            backgroundHistoryImg.src = "mtnGallery2.jpg"
            histContent.style.backgroundColor = "aliceblue"
            histContent.style.opacity = 0.8
        }

        for (dot in dots){
            if(dots[dot].id==e.target.id){
                dots[dot].style.fill = "black"
            }
            else{
                dots[dot].style.fill = "white"
            }
        }

    })
})
histPage.addEventListener('click',() =>{
    backgroundHistoryImg.src="mtn2.jpg"
    histContent.style.backgroundColor = "transparent" 
    histContent.style.opacity = 1
    histContent.style.padding = "0px"
})

//landing page text zoom anim//

let container = document.querySelector(".txtContainer")
let sec = document.querySelector(".secTitle")
addEventListener('scroll',(e)=>{
    container.style.scale = 1 - (window.pageYOffset * 0.001)
})

//snapping to sections effect
function snapToHistory(){
    window.scrollBy(0,sec.getBoundingClientRect().y);
}

//fade in on view animation
const histText = document.querySelector(".histText")
const obs= new IntersectionObserver((e) =>{
    e.forEach((thing) => {
        if (thing.isIntersecting==true){
            thing.target.classList.add("show")   
        }
        else{
            thing.target.classList.remove("show") 
        }
    })
})
obs.observe(sec)
obs.observe(histText)
//accordion show
const acc = document.querySelector(".accordion")
const menuItems = document.querySelectorAll(".menuItems")
function showMenu(){
    Array.from(menuItems).forEach((t)=>{
        if(t.style.display =="inline" && window.innerWidth<=575){t.style.display = "none"}
        else{t.style.display = "inline"}
    })
}
window.addEventListener('resize',()=>{
    Array.from(menuItems).forEach((t)=>{
        if (t.style.display == "none" && window.innerWidth > 575){t.style.display = "inline"}
})})

