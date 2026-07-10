import FutureCard from "./FutureCard";
import Buttons from "./Buttons";


function FutureResult({future}){


    const text = future.future;


    const sections = text.split(/\d+\.\s/);


    return(

        <div className="result">


            <h1>
                {future.message}
            </h1>



            <FutureCard

                icon="🚀"

                year="5"

                text={sections[1] || text}

            />



            <FutureCard

                icon="🌎"

                year="10"

                text={sections[2] || "Your journey continues..."}

            />



            <FutureCard

                icon="🏆"

                year="15"

                text={sections[3] || "You achieve your dreams..."}

            />



            <Buttons future={future.future}/>


        </div>

    )

}


export default FutureResult;