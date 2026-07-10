import { useState } from "react";

import Navbar from "./components/Navbar";
import Hero from "./components/Hero";
import UserForm from "./components/UserForm";
import FutureResult from "./components/FutureResult";
import Loading from "./components/Loading";
import Footer from "./components/Footer";

import "./App.css";


function App(){

    const [future,setFuture] = useState(null);

    const [loading,setLoading] = useState(false);


    return(

        <div>

            <Navbar />

            <Hero />

            <UserForm
                setFuture={setFuture}
                setLoading={setLoading}
            />


            {
                loading && <Loading />
            }


            {
                future &&
                <FutureResult future={future}/>
            }


            <Footer />

        </div>

    );

}


export default App;