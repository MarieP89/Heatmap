import React, {useState} from 'react';
import Calendar from "react-calendar";
import "react-calendar/dist/Calendar.css";

import './App.css';

function App() {

  const [selectedDate, setSelectedDate] = useState(new Date());

  const handleDateChange = date => {
    setSelectedDate(date);
  }

  return (
      <div className="calender-container">
        <h1>Kalender um meine Schüler zu stalken</h1>
        <Calendar
            onChange={handleDateChange}
            value={selectedDate}
        />
        <p>Ausgewähltes Datum: {selectedDate.toLocaleDateString()}</p>
      </div>
  );
}

export default App;
