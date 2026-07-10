import jsPDF from "jspdf";


function Buttons({future}){


function copyText(){

navigator.clipboard.writeText(future);

alert("Copied Successfully!");

}



function downloadPDF(){

const pdf = new jsPDF();


pdf.setFontSize(18);

pdf.text(
"FutureMe AI Report",
20,
20
);


pdf.setFontSize(12);


const lines = pdf.splitTextToSize(
future,
170
);


pdf.text(
lines,
20,
40
);



pdf.save(
"FutureMe_Report.pdf"
);


}



function reset(){

window.location.reload();

}



return(

<div className="buttons">


<button onClick={copyText}>
📋 Copy
</button>


<button onClick={downloadPDF}>
📄 Download PDF
</button>


<button onClick={reset}>
🔄 Reset
</button>


</div>

)

}


export default Buttons;