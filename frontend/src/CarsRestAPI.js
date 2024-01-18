// zaimportuj potrzebne hooki
import React, {useEffect, useState} from "react";

import axios from "axios";

// stwórz factory function, które zwróci obiekt hooka use state na produkty, metodę pobierania jednego, dodawania i usuwania produktu

const useCarRestApi = () => {
    let [cars, setCars] = useState([])
    // zmienna change będzie wskaźnikiem, czy usunęliśmy jakiś samochód

    let [change, setChange] = useState(true)

    // useEfect, który reaguje na zmianę change i reakcją jest pobranie wszystkich produktów
    // logika:
    // 1. tworzę funkcję getData(), która wywołuje asynchroniczną getAll()
    // 2. wywołuję i staram się łapać errory
    // 3. ustawiam change na false po wykonaniu
    useEffect(() => {
        async function getData() {
            await getAll();
        }

        getData().catch(err => console.log(err))
        setChange(false)
    }, [change]);


    // tworzę zmienną, która przechowuje bazowy url
    const BASE_URL = 'http://localhost:8001/car'

    // --------------------------------------------------
    // SEKCJA METOD DO ZARZĄDZANIA REQUESTAMI
    // --------------------------------------------------
    const getAll = async () => {
        const response = await axios.get(`http://localhost:8000/cars/all`)
        setCars(await response.data['all_cars'])
    }

    const getOne = async (id) => {
        let car
        if (change) {
            const response = await axios.get(`${BASE_URL}/${id}`)
            car = await response.data
            return car
        }
        const foundCars = cars.filter(c => c.id === id)
        car = foundCars.length === 0 ? {} : foundCars[0]
        console.log(car)
        return car
    }

    const validate = (car) => {
        const errors = []

        const stringHasLength = (expression, desiredLength) => {
            return typeof expression === 'string' || expression.length === desiredLength
        }

        const hasType = (value, type) => {
            return typeof value === type
        }

        const isString = (expression) => {
            return hasType(expression, 'string')
        }

        const isInteger = (value) => {
            return hasType(value, 'number') && Number(value.toFixed()) === value
        }

        const inRange = (value, min, max) => {
            return value >= min && value <= max;
        }

        const matchesRegex = (expression, regex) => {
            return regex.test(expression)
        }

        const addErrorIfExist = (errorCheckValue, errorMsg) => {
            if (errorCheckValue) {
                errors.push(errorMsg)
            }
        }

        addErrorIfExist([null, undefined].includes(car), 'Car is null')

        addErrorIfExist(!stringHasLength(car.registration, 7), 'Invalid car registration')
        addErrorIfExist(!stringHasLength(car.vin, 17), 'Invalid car vin')
        addErrorIfExist(!isString(car.make), 'Invalid car make')
        addErrorIfExist(!isString(car.model), 'Invalid car model')
        addErrorIfExist(!matchesRegex(car.first_registration_date, /^\d{4}-\d{2}-\d{2}$/), 'Invalid first registration date format')
        addErrorIfExist(!isInteger(car.production_year), 'Production year must be an integer')
        addErrorIfExist(!isInteger(car.mileage) || !inRange(car.mileage, 0, 6000000), 'Mileage has to be integer between 0 and 6 000 000')
        addErrorIfExist(!isInteger(car.fuel_type_id) || !inRange(car.fuel_type_id, 0, Infinity), 'Fuel type id has to be integer between 0 and Infinity')
        addErrorIfExist(!isInteger(car.vehicle_status_id) || !inRange(car.vehicle_status_id, 0, Infinity), 'Mileage has to be integer between 0 and Infinity')

        return errors
    }

    const add = async (car) => {
        const errors = validate(car)
        if (errors.length !== 0) {
            return errors.join(' ')
        }

        const response = await axios.post(`${BASE_URL}/0`, car);
        setChange(true)
        return await response.data
    }

    const remove = async (id) => {
        const response = await axios.delete(`${BASE_URL}/${id}`);
        setChange(true);
        return await response.data;
    }

    return [cars, getOne, add, remove]

}

const Car = ({car, getOne, remove}) => (
    <div className="card my-2">
        <div className='card-body'>
            <h1 className='card-title'>ID:    {car.id}</h1>
            <h1 className='card-title'>REGISTRATION:    {car.registration}</h1>
            <h1 className='card-title'>VIN:    {car.vin}</h1>
        </div>
        <div className="my-3">
            <button
                className="btn btn-primary me-2"
                onClick={() => getOne(car.id)}
            >Details
            </button>

            <button
                className="btn btn-secondary"
                onClick={() => remove(car.id)}
            >Remove
            </button>
        </div>
    </div>
)

const CarsRestAPI = () => {
    let [cars, getOne, add, remove] = useCarRestApi()

    const addCar = async () => {
        const car = {"registration": "WA38902", "vin": "VF3MJEHZRJS446752", "make": "Peugeot", "model": "308", "first_registration_date": "2017-08-21", "production_year": 2017, "mileage": 150000, "fuel_consumption": 6.99, "fuel_type_id": 1, "vehicle_status_id": 1}
        console.log('id or message:', await add(car))
    }

    return (
        <div>
            {
                cars.map(car => <Car
                    key={car.id}
                    car={car}
                    getOne={getOne}
                    remove={remove}
                />)
            }
            <div>
                <button
                    className="mt-3 btn btn-success"
                    onClick={() => addCar()}
                >Add New Car</button>
            </div>
        </div>
    )

}
export default CarsRestAPI