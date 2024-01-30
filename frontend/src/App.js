import React, {useState, useEffect} from 'react';
import Calendar from "react-calendar";
import "react-calendar/dist/Calendar.css";
import axios from "axios";

import './App.css';

function App() {

  const [selectedDate, setSelectedDate] = useState(new Date());
  const [dropDown, setDropDown] = useState([]);
  const [data, setData] = useState([]);
  const [selectedValue, setSelectedValue] = useState(' ');

  // useEffect(()=> {
  //     fetchDropdownData();
  // }, []);
  //
  // const fetchDropdownData = async () => {
  //  try {
  //   const response = await axios.get('/path/to/your/api', {
  //      responseType: "text"
  //   });
  //   const data = response.data;
  //   setDropDown(data);
  //  }catch (error){
  //      console.error('Error fetching the data', error)
  //  }
  // };

    // useEffect(() => {
    //     axios.get('./data.txt')
    //         .then(response =>{
    //             const lines = response.data.split('\n');
    //             const headers = lines[0].split(',');
    //
    //             const data = lines.slice(1).map(line => {
    //                 const values = line.split(',');
    //                 let obj = {};
    //                 headers.forEach((header, i) =>{K
    //                     obj[header] = values[i];
    //                 });
    //                 return obj;
    //             });
    //             const filteredData = data.filter(item => item['Langname'] && item['Vorname']);
    //             setDropDown(filteredData)
    //         })
    //         .catch(error => console.error('Error fetching the data', error));
    // }, []);

    useEffect(() => {
        axios.get('http://localhost:5000/read-csv')
            .then(response => {
                const filteredData = response.data.map(item => {
                    return { name: item.name };  // Replace 'name' with the actual property name
                });
                setData(filteredData);
            })
            .catch(error => {
                console.error('Error fetching the CSV data', error);
            });
    }, []);




    const handleDateChange = date => {
    setSelectedDate(date);
  }

    const handleDropdownChange = (event) => {
        setSelectedValue(event.target.value);
    };

  return (
      <div className="calender-container">
        <h1>Kalender um meine Schüler zu stalken</h1>
          <div>
              <select onChange={handleDropdownChange}>
                  {dropDown.map((item, index) => (
                      <option key={index} value={index}>{item['Langname']} {item['Vorname']}</option>
                      ))}
              </select>
          </div>
        <Calendar
            onChange={handleDateChange}
            value={selectedDate}
        />
        <p>Ausgewähltes Datum: {selectedDate.toLocaleDateString()}</p>
         <p>Select Name: {dropDown[selectedValue] ? `${dropDown[selectedValue]['Langname']} ${dropDown[selectedValue]['Vorname']}` : ''}</p>
      </div>
  );
}

export default App;
