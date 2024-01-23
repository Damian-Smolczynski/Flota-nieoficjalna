import {useEffect, useState} from "react";
import axios from "axios";

const useCarsRestApi = () => {
    let [cars, setCars] = useState([])
    let [change, setChange] = useState(true)


    useEffect(() => {
        async function getData() {
            await getAll();
        }

        getData().catch(err => console.log(err))
        setChange(false)
    }, [change]);

    const BASE_URL = 'http://localhost/cars'

    const getAll = async () => {
        const response = await axios.get(`${BASE_URL}/all`)
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
        addErrorIfExist(!isInteger(Number(car.production_year)), 'Production year must be an integer')
        addErrorIfExist(!isInteger(Number(car.mileage)) || !inRange(Number(car.mileage), 0, 6000000), 'Mileage has to be integer between 0 and 6 000 000')
        addErrorIfExist(!isInteger(Number(car.fuel_type_id)) || !inRange(car.fuel_type_id, 0, Infinity), 'Fuel type id has to be integer between 0 and Infinity')
        addErrorIfExist(!isInteger(Number(car.vehicle_status_id)) || !inRange(car.vehicle_status_id, 0, Infinity), 'Mileage has to be integer between 0 and Infinity')

        return errors
    }

    const add = async (car) => {
        const errors = validate(car)
        if (errors.length !== 0) {
            return errors.join(' ')
        }

        const response = await axios.post(`${BASE_URL}/`, car);
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

export default useCarsRestApi