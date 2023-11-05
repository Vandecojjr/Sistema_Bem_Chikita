var menuItem = document.querySelectorAll('.item-menu')

function selectlink(){
    menuItem.forEach((item)=>
        item.classList.remove('ativo')
    )
        this.classList.add('ativo')
}

menuItem.forEach((item)=>
item.addEventListener('click',selectlink)
)

//expandir menu

var expBtn = document.querySelector('#btn-exp')
var menuSide = document.querySelector('.menu-lateral')

expBtn.addEventListener('click', function(){
    menuSide.classList.toggle('expandir')
})