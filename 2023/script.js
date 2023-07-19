var nbsp = document.getElementById('nbsp');
var click = 0;

nbsp.addEventListener('click', function(){
    clickcount()
})

function clickcount(){
    click++;
    if (click >= 5){
        alert('giga@hcu.hs.kr로 이 화면을 캡쳐해서 보내주시면 선착순 3명에게 선물을!')
        click = 0
    }
}