import { useState } from "react";
import axios from "axios";


function UserForm({ setFuture, setLoading }) {


    const [data, setData] = useState({

        name: "",
        age: "",
        goal: "",
        skills: ""

    });



    function handleChange(e) {

        setData({

            ...data,

            [e.target.name]: e.target.value

        });

    }




    async function generateFuture() {


        try {


            setLoading(true);



            const response = await axios.post(

                "https://futureme-backend-a6ox.onrender.com/api/future/",

                data

            );



            setFuture(response.data);



        }

        catch(error) {


            console.log(error);


            alert("Server error");


        }


        finally {


            setLoading(false);


        }


    }




    return (


        <div className="form-card">


            <h2>
                Tell About Yourself ✨
            </h2>



            <input

                name="name"

                placeholder="👤 Name"

                value={data.name}

                onChange={handleChange}

            />



            <input

                name="age"

                placeholder="🎂 Age"

                value={data.age}

                onChange={handleChange}

            />



            <input

                name="goal"

                placeholder="🎯 Goal"

                value={data.goal}

                onChange={handleChange}

            />



            <input

                name="skills"

                placeholder="💡 Skills"

                value={data.skills}

                onChange={handleChange}

            />



            <button onClick={generateFuture}>

                Generate My Future 🚀

            </button>



        </div>


    );


}


export default UserForm;