import React, {useState, useEffect} from 'react';
import Calendar from "react-calendar";
import "react-calendar/dist/Calendar.css";
import axios from "axios";

import './App.css';

function App() {

  const [selectedDate, setSelectedDate] = useState(new Date());
  const [data, setData] = useState([]);
  const [selectedKlasse, setSelectedKlasse] = useState(' ');
  const [klassen, setKlassen] = useState([]);
  const [langnames, setLangnames] = useState([]);
  const [selectedLangname, setSelectedLangname] = useState('');


    // useEffect(() => {
    //     axios.get('http://localhost:5000/read-csv')
    //         .then(response => {
    //             const filteredData = response.data.map(item => {
    //                 return { name: item.name };  // Replace 'name' with the actual property name
    //             });
    //             setData(filteredData);
    //         })
    //         .catch(error => {
    //             console.error('Error fetching the CSV data', error);
    //         });
    // }, []);

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

    const fetchLangnames = (selectedKlasse) => {
        // Fetch the "Langname" values based on the selected "Klasse" from the backend
        axios
            .get(`http://localhost:5000/get-langnames?klasse=${selectedKlasse}`)
            .then((response) => {
                setLangnames(response.data);
            })
            .catch((error) => {
                console.error('Error fetching Langnames data', error);
            });
    };

  return (
      <div className="calender-container">
          <h1>Kalender um meine Schüler zu stalken</h1>
          <div>
              <select onChange={handleKlasseChange} value={selectedKlasse}>
                  {klassen.map((klasse, index) => (
                      <option key={index} value={klasse}>{klasse}</option>
                  ))}
              </select>
          </div>
          <div>
              <select onChange={handleLangnameChange} value={selectedLangname}>
                  {langnames.map((langname, index) => (
                      <option key={index} value={langname}>{langname}</option>
                  ))}
              </select>
          </div>
          <Calendar
              onChange={handleDateChange}
              value={selectedDate}
          />
          <p>Ausgewähltes Datum: {selectedDate.toLocaleDateString()}</p>
      </div>
  );
}

export default App;
