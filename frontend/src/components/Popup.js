import React from "react";
import "../stylesheets/popup.css"

export const InputDiv = ({labelText, type, id_, description, onChangeFn}) => {
    return (
        <div className="mb-3">
            <label htmlFor={id_} className="form-label">{labelText}</label>
            <input type={type} className="form-control" id={id_}
                   aria-describedby="usernameHelp" onChange={(e) => onChangeFn(e.target.value)}/>
            {description && <div id={`${id_}Help`} className="form-text">{description}</div>}
        </div>
    )
}

const Popup = () => {

    return (
        <section>
            <div className="container">
                <button id="open-popup" onClick={() => document.querySelector(".popup").classList.add("active")}>Activate</button>
            </div>
            <div className={"popup"}>
                <div className={'close-btn'} onClick={() => document.querySelector(".popup").classList.remove("active")}>&times;</div>
                <h1>Add New Car</h1>
                <p>Loremsdassda
                dsaasdasdasdas
                d
                asd
                asd
                as
                das
                d
                asd
                asd
                d</p>
            </div>

        </section>

    )
}

export default Popup