import React, { useEffect, useState } from 'react';
import axios from 'axios';

function PatientList() {
  const [patients, setPatients] = useState([]);

  useEffect(() => {
    axios.get('http://127.0.0.1:8000/api/patients/')
      .then(response => setPatients(response.data))
      .catch(error => console.error(error));
  }, []);

  return (
    <div>
      <h2>قائمة المرضى</h2>
      <ul>
        {patients.map(patient => (
          <li key={patient.id}>
            {patient.full_name} - {patient.birth_date} - {patient.gender}
          </li>
        ))}
      </ul>
    </div>
  );
}

export default PatientList;
