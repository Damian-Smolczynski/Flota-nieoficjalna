import React from "react";
import "../stylesheets/AddCarPopup.css"
import {useKey} from "react-use"
import { useForm } from "react-hook-form"



const AddCarPopup = ({add}) => {

    useKey("Escape", () => document.querySelector(".popup").classList.remove("active"));

    // npm install react-hook-form
    const {
        register,
        handleSubmit,
        // watch,
        formState: { errors },
    } = useForm()

    const addCar = async (car) => {
        const response = await add(car)
        if (typeof response === 'number') {
            document.querySelector(".popup").classList.remove("active")
        }
    }

    const onSubmit = (data) => {
        if (Object.entries(data).filter(arr => arr[1] !== '').length < Object.entries(data).length) {
            console.log(data)
            alert('Waiting for data')
        }
        addCar(data)
    }

    return (
        <section>
            <div className="container">
                <button id="open-popup" onClick={() => document.querySelector(".popup").classList.add("active")}>Activate</button>
            </div>
            <div className={"popup"}>
                <div className={'close-btn'}
                     onClick={() => document.querySelector(".popup").classList.remove("active")}>&times;</div>
                <h1>Add New Car</h1>

                <form onSubmit={handleSubmit(onSubmit)}>
                    <p className={"formInputHeader"}>Registration:</p>
                    <input className={"addCarInput"} {...register("registration", {pattern: {value: /^[A-Z0-9]{7}$/, message: "Registration must contain only large letters and digits and be 7 chars long"}})}/>
                    {errors.registration && <p className={"formErrMsg"}>{errors.registration?.message}</p>}


                    <p className={"formInputHeader"}>VIN:</p>
                    <input className={"addCarInput"} {...register("vin", {pattern: {value: /^[A-Z0-9]{17}$/, message: "Registration must contain only large letters and digits and be 17 chars long"}})}/>
                    {errors.vin && <p className={"formErrMsg"}>{errors.vin.message}</p>}

                    <p className={"formInputHeader"}>Make:</p>
                    <input className={"addCarInput"} {...register("make", {pattern: {value: /^[A-Z]+( [A-Z]+)?$/, message: "Make must contain only large letters and might have one space"}})}/>
                    {errors.make && <p className={"formErrMsg"}>Registration must contain seven A-Z 0-9</p>}

                    <p className={"formInputHeader"}>Model:</p>
                    <input className={"addCarInput"} {...register("model", {pattern: {value: /^([A-Z0-9]+( [A-Z0-9]+)?)+$/, message: "Registration must contain only large letters, digits and spaces"}})}/>
                    {errors.model && <p className={"formErrMsg"}>{errors.model.message}</p>}

                    <p className={"formInputHeader"}>First registration date:</p>
                    <input className={"addCarInput"} type={"date"} {...register("first_registration_date")}/>

                    <p className={"formInputHeader"}>Production year:</p>
                    <input className={"addCarInput"} type={"number"} {...register("production_year", {pattern: {value: /^[0-9]{4}$/, message: "Production year must be in YYYY format"}})}/>
                    {errors.production_year && <p className={"formErrMsg"}>{errors.production_year.message}</p>}

                    <p className={"formInputHeader"}>Mileage:</p>
                    <input className={"addCarInput"} type={"number"} {...register("mileage", {min: {value: 0, message: 'Mileage needs to be grater than 0'}, max: {value: 6000000, message: 'Mileage needs to be lower than 6 000 000'}})}/>
                    {errors.mileage && <p className={"formErrMsg"}>{errors.mileage.message}</p>}

                    <p className={"formInputHeader"}>Fuel consumption:</p>
                    <input className={"addCarInput"} type={"number"} step={"0.01"} {...register("fuel_consumption", {min: {value: 0, message: 'Fuel consumption needs to be grater than 0'}, max: {value: 100, message: 'Fuel consumption to be lower than 100'}})}/>
                    {errors.fuel_consumption && <p className={"formErrMsg"}>{errors.fuel_consumption.message}</p>}

                    <p className={"formInputHeader"}>Fuel type:</p>
                    <select {...register("fuel_type_id", {required: true})}>
                        <option value="1">Petrol</option>
                        <option value="2">Diesel</option>
                        <option value="3">Electric</option>
                    </select>
                    {errors.production_year && <p className={"formErrMsg"}>{errors.production_year.message}</p>}

                    <p className={"formInputHeader"}>Vehicle status:</p>
                    <select {...register("vehicle_status_id", {required: true})}>
                        <option value="1">Ready to use</option>
                        <option value="2">Waiting for repairs to be done</option>
                        <option value="3">Waiting for mot or insurance</option>
                    </select>
                    {errors.production_year && <p className={"formErrMsg"}>{errors.production_year.message}</p>}
                    <div className={"buttons"}>
                        <button type={"submit"}>Create</button>
                    </div>

                </form>
            </div>

        </section>

)
}

export default AddCarPopup