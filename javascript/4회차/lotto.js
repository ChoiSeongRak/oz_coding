const todaySpan = document.querySelector("#today")
const numbersDiv = document.querySelector(".numbers")
const drawButton = document.querySelector("#draw")
const resetButton = document.querySelector("#reset")





const today = new Date()
let year = today.getFullYear()
let month = today.getMonth() +1
let date = today.getDate()
todaySpan.textContent = `${year}년 ${month}월 ${date}일 `


function paintNumber(number){
    const eachNumDiv = document.createElement("div")
    eachNumDiv.classList.add("eachnum")
    eachNumDiv.textContent = number
    numbersDiv.append(eachNumDiv)
}
//클릭하면 랜덤숫자 여섯개ㅏ배열에 추가된다.
drawButton.addEventListener("click", function(){
    let lottoNumbers = []
    numbersDiv.innerHTML ="";
    while(lottoNumbers.length < 6){
        let rn = Math.floor(Math.random() * 45 + 1)
        if(lottoNumbers.indexOf(rn) === -1)
        lottoNumbers.push(rn)
        paintNumber(rn)
    
    }
    console.log(lottoNumbers)
})

resetButton.addEventListener("click", function(){
    lottoNumbers.splice(0, 6) //splice: (시작하는 인덱스 위치, 몇개를 지울지 개수)
    
})