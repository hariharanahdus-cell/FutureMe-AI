function FutureCard({icon, year, text}){


    return(

        <div className="future-card">


            <h2>
                {icon} After {year} Years
            </h2>


            <p>
                {text}
            </p>


        </div>

    )

}


export default FutureCard;