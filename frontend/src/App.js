import React, {useState, useEffect} from 'react';
import Calendar from "react-calendar";
//import "react-calendar/dist/Calendar.css";
import axios from "axios";

import "./Calender.css";
import './App.css';
import {format, isWithinInterval, startOfDay, endOfDay} from 'date-fns';

function App() {

    const [selectedDate, setSelectedDate] = useState(new Date());
    const [data, setData] = useState([]);
    const [selectedKlasse, setSelectedKlasse] = useState(' ');
    const [klassen, setKlassen] = useState([]);
    const [langnames, setLangnames] = useState([]);
    const [selectedLangname, setSelectedLangname] = useState('');
    const [absences, setAbsences] = useState([]);


    useEffect(() => {
        axios.get('http://localhost:5000/read-csv')
            .then(response => {
                setData(response.data);
            })
            .catch(error => {
                console.error('Error fetching the CSV data', error);
            });
    }, []);

    useEffect(() => {
        axios.get('http://localhost:5000/get-klassen')
            .then(response => {
                setKlassen(response.data);
            })
            .catch(error => {
                console.error('Error fetching the Klassen data', error);
            });
    }, []);

    useEffect(() => {
        fetchLangnames(selectedKlasse);
    }, [selectedKlasse]);

    useEffect(() => {
        axios.get(`http://localhost:5000/get-absences?langname=${selectedLangname}`)
            .then(response => {
                setAbsences(response.data);
                console.log(response.data);
            })
            .catch(error => {
                console.error('Error fetching the absences data', error);
            });
    }, [selectedLangname]);


    const handleDateChange = date => {
        setSelectedDate(date);
    }

    const handleKlasseChange = (event) => {
        setSelectedKlasse(event.target.value);
    };

    const handleLangnameChange = (event) => {
        const selectedLangname = event.target.value;
        setSelectedLangname(selectedLangname);
    };

    // const fetchData = async (selectedKlasse) => {
    //     const responseAbsences = await axios.get(`http://localhost:5000/get-absences?langname=${selectedLangname}`);
    //     setAbsences(responseAbsences.data);
    // };

    const fetchLangnames = (selectedKlasse) => {
        axios
            .get(`http://localhost:5000/get-langnames?klasse=${selectedKlasse}`)
            .then((response) => {
                setLangnames(response.data);
            })
            .catch((error) => {
                console.error('Error fetching Langnames data', error);
            });
    };

    const convertDateString = (dateString) => {
        const [day, month, year] = dateString.split('.');
        return new Date(`${year}-${month}-${day}`);
    };


    const tileClassName = ({date, view}) => {
        if (view === 'month') {
            const checkDate = startOfDay(date);

            const absence = absences.find(absence => {
                const beginDate = startOfDay(convertDateString(absence.Beginndatum));
                const endDate = endOfDay(convertDateString(absence.Enddatum));
                return isWithinInterval(checkDate, {start: beginDate, end: endDate});
            });
            if (absence) {
                return `absence-${absence.Abwesenheitsgrund}`;
            }
        }
    };


    return (
        <div className="calender-container">
            <h1>Kalender</h1>
            <div style={{ display: 'flex', gap: '20px' }}>
                <div>
                    <label htmlFor="klasse-select">Klasse:</label>
                    <select onChange={handleKlasseChange}
                            value={selectedKlasse}
                            style={{width: "200px"}}
                    >
                        <option value="">Wähle Klasse</option>
                        {klassen.map((klasse, index) => (
                            <option key={index} value={klasse}>{klasse}</option>
                        ))}
                    </select>
                </div>
                <div>
                    <label htmlFor="klasse-select">Schüler:</label>
                    <select onChange={handleLangnameChange}
                            value={selectedLangname}
                            style={{width: "200px"}}
                    >
                        {langnames.map((langname, index) => (
                            <option key={index} value={langname}>{langname}</option>
                        ))}
                    </select>
                </div>
            </div>
            <Calendar
                onChange={handleDateChange}
                value={selectedDate}
                tileClassName={tileClassName}
            />
            <p>Ausgewähltes Datum: {selectedDate.toLocaleDateString()}</p>
        </div>
    );
}

export default App;
