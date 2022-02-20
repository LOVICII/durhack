const url = "http://127.0.0.1:8080/";
let coloured = false;
mainImgId = ""
// function loadMainImgs(){
//     mainImg = document.getElementById("mainImg");
//     img1 = document.getElementById("relImg1");
//     img2 = document.getElementById("relImg2");
//     img3 = document.getElementById("relImg3");
//     img4 = document.getElementById("relImg4");

//     urls = ["http://127.0.0.1:8080/imgfile?id=blac0001","http://127.0.0.1:8080/imgfile?id=blac0002","http://127.0.0.1:8080/imgfile?id=blac0003","http://127.0.0.1:8080/imgfile?id=blac0004","http://127.0.0.1:8080/imgfile?id=blac0005"]
//     fetches = []
//     imgArray = []
//     for(let i=0; i<urls.length; i++){
//         fetches.push(
//             fetch(urls[i])
//             .then(response => response.blob())
//             .then(imageBlob => {
//                 // Then create a local URL for that image and print it 
//                 const imageObjectURL = URL.createObjectURL(imageBlob);
//                 imgArray.push(imageObjectURL);
//                 console.log(imageObjectURL);
//             })
//         )
//     }

//     Promise.all(fetches).then(function(){
//         mainImg.src = imgArray[0];
//         img1.src = imgArray[1]
//         img2.src = imgArray[2]
//         img3.src = imgArray[3]
//         img4.src = imgArray[4]
//     })
// }


function loadImgs(target) {
    mainImg = document.getElementById("mainImg");
    img1 = document.getElementById("relImg1");
    img2 = document.getElementById("relImg2");
    img3 = document.getElementById("relImg3");
    img4 = document.getElementById("relImg4");
    url_file = url + "imgfile?id=" + target;
    url_info = url + "imginfo?id=" + target;
    fetches = []
    imgArray = []
    relImgs = []
    fetches.push(
        fetch(url_file)
            .then(res => res.blob())
            .then(imageBlob => {
                const imageObjectURL = URL.createObjectURL(imageBlob);
                imgArray.push(imageObjectURL);
                mainImgId = target;
            })
    );


    fetch(url_info)
        .then(res => res.json())
        .then(body => {
            console.log(body["relative"][0])
            for (let i = 0; i < 4; i++) {
                relImgs.push(body["relative"][i])
            }
            document.getElementById("description").innerHTML = body["description"];
            document.getElementById("title").innerHTML = body["title"];
        })
        .then(()=>{
            for (let i = 0; i < 4; i++) {
                relimg_url = url + "imgfile?id=" + relImgs[i]
                fetches.push(
                    fetch(relimg_url)
                        .then(response => response.blob())
                        .then(imageBlob => {
                            // Then create a local URL for that image and print it 
                            const imageObjectURL = URL.createObjectURL(imageBlob);
                            imgArray.push(imageObjectURL);
                            console.log(imageObjectURL);
                        })
                )
            }
        
            Promise.all(fetches).then(function () {
                mainImg.src = imgArray[0];
                img1.src = imgArray[1]
                img2.src = imgArray[2]
                img3.src = imgArray[3]
                img4.src = imgArray[4]
            })
        })
}

function colourize(){
    if (coloured == false){
        fetch(url+"imgfilecolour?id="+mainImgId)
            .then(res => res.blob())
            .then(imageBlob => {
                const imageObjectURL = URL.createObjectURL(imageBlob);
                document.getElementById("mainImg").src = imageObjectURL;
                document.getElementById("btnColor").innerHTML = "original";
                console.log(imageObjectURL);
                coloured = true;
            })
    }else{
        fetch(url+"imgfile?id="+mainImgId)
        .then(res => res.blob())
        .then(imageBlob => {
            const imageObjectURL = URL.createObjectURL(imageBlob);
            document.getElementById("mainImg").src = imageObjectURL;
            document.getElementById("btnColor").innerHTML = "colourize";
            console.log(imageObjectURL);
            coloured = false;
        })
    }
}

document.addEventListener("DOMContentLoaded", function(){
    loadImgs("blac0001");
});