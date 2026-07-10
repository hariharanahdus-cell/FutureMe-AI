import FutureCard from "./FutureCard";
import Buttons from "./Buttons";


function FutureResult({future}){


    const text = future.future;


    const sections = text.split(/After \d+ Years:/);



    return(

        <div className="result">


            <h1>
                {future.message}
            </h1>



            <FutureCard

                icon="🚀"

                year="5"

                text={sections[1]}

            />



            <FutureCard

                icon="🌎"

                year="10"

                text={sections[2]}

            />



            <FutureCard

                icon="🏆"

                year="15"

                text={sections[3]}

            />


            <Buttons future={future.future}/>


        </div>

    )

}


export default FutureResult;