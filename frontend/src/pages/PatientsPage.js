import React, { useState } from 'react';
import PatientList from '../components/patients/PatientList';
import AddPatientForm from '../components/patients/AddPatientForm';

function PatientsPage() {
  const [refresh, setRefresh] = useState(false);

  const reload = () => setRefresh(!refresh);

  return (
    <div>
      <h1>إدارة المرضى</h1>
      <AddPatientForm onAdded={reload} />
      <PatientList key={refresh} />
    </div>
  );
}

export default PatientsPage;
