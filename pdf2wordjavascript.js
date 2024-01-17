// async function convertToWord(){
//     const pdfFile = document.getElementById('pdfFile').files[0];

//     if (!pdfFile){
//         alert('Wrong file selected. Please select a pdf file.');
//     };

//     return;
// }

// const reader = new FileReader();
// reader.onload = async function(event){

//     try{
//         const pdfDoc = await PDFLib.PDFDocument.load(pdfDataUri);

//         const wordDoc = await PDFLib.convertToWord(pdfDoc);
//         const wordBytes = await wordDoc.save();
//         const blob = new Blob([wordBytes], { type: 'application/msword'});
//         saveAs(blob, 'converted.docx');
//     }

//     catch(error){
//         console.error(error);
//         alert('Conversion failed, please try again');
//     }
// };

// reader.readAsDataURL(pdfFile);

