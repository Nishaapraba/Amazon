outer: for(let i=1;i<10;i++){
    console.log("i="+i)
    if(i==5){
        break
    }
inner: for(j=1;j<7;j++){
    if(j==3) break
    console.log("j="+j)

}
}