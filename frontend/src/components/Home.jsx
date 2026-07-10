import { useState } from "react";

import Navbar from "./Navbar";
import Hero from "./Hero";
import UserForm from "./UserForm";
import FutureResult from "./FutureResult";
import Loading from "./Loading";
import Footer from "./Footer";


function Home(){

  const [future,setFuture] = useState(null);

  const [loading,setLoading] = useState(false);


  return(

    <div>

      <Navbar/>

      <Hero/>


      <UserForm
        setFuture={setFuture}
        setLoading={setLoading}
      />


      {
        loading && <Loading/>
      }


      {
        future && 
        <FutureResult future={future}/>
      }


      <Footer/>

    </div>

  );

}


export default Home;