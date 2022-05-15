//画像をアップロードしたらプレビューを表示
function previewFile(){
    const file = document.getElementById('inputImage').files[0];
    const preview = document.querySelector('img');
    const reader = new FileReader();

    reader.onload = function(e) {
        preview.src = reader.result;
    }
    reader.readAsDataURL(file);
}

//送信前の確認
const submitCheck = () => {
    let fileInput = document.getElementById('inputImage');
    const files = fileInput.files;

    const fileLength = files.length;
    console.log(fileLength);
    if(fileLength >= 1){
        alert('実行します');
    }else{
        alert('ファイルが選択されていません');
    }
}


let submitButton = document.getElementById('submit');
submitButton.addEventListener('click', submitCheck);

