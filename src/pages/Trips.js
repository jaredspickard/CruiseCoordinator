import React, { useState } from 'react';
import FormControl from '@mui/material/FormControl';
import Input from '@mui/material/Input';
import InputLabel from '@mui/material/InputLabel';
import Button from '@mui/material/Button';
import TripList from '../components/TripList';

export default function Trips() {

    const [tripName, setTripName] = useState("");

    const handleTripNameChange = (event) => {
        setTripName(event.target.value);
    }

    const handleTripCreation = async () => {
        // TODO: ensure tripName is not empty
        const resp = await fetch('/api/trips/create', {
            method: 'POST',
            body: JSON.stringify({
                trip_name: tripName
            }),
            headers: {
                'Content-Type': 'application/json'
            }
        });
        const data = await resp.json();
        console.log(data);
        setTripName("");
    }

    return (
        <div>
            <h2>Trips Page</h2>
            <FormControl variant="standard">
                <InputLabel htmlFor="component-simple">TripName</InputLabel>
                <Input id="create-trip-name" value={tripName} onChange={handleTripNameChange} />
            </FormControl>
            <Button onClick={handleTripCreation}>Create Trip</Button>
            <TripList />
        </div>
    )
}
