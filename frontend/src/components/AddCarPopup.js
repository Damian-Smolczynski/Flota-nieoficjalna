import React from "react";
import "../stylesheets/popup.css"
import {useKey} from "react-use"


const AddCarPopup = () => {

    useKey("Escape", () => document.querySelector(".popup").classList.remove("active"));

    return (
        <section>
            <div className="container">
                <button id="open-popup" onClick={() => document.querySelector(".popup").classList.add("active")}>Activate</button>
            </div>
            <div className={"popup"}>
                <div className={'close-btn'} onClick={() => document.querySelector(".popup").classList.remove("active")}>&times;</div>
                <h1>Add New Car</h1>
                <p>Loremsdassda</p>
            </div>

        </section>

    )
}

export default AddCarPopup