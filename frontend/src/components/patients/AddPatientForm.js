import React, { useState } from 'react';
import axios from 'axios';

function AddPatientForm({ onAdded }) {
  const [formData, setFormData] = useState({
    full_name: '',
    birth_date: '',
    gender: ''
  });

  const handleChange = e => {
    setFormData({...formData, [e.target.name]: e.target.value});
  };

  const handleSubmit = e => {
    e.preventDefault();
    axios.post('http://127.0.0.1:8000/api/patients/', formData)
      .then(() => {
        onAdded(); // لإعادة تحميل القائمة بعد الإضافة
        setFormData({ full_name: '', birth_date: '', gender: '' });
      })
      .catch(error => console.error(error));
  };

  return (
    <form onSubmit={handleSubmit}>
      <h3>إضافة مريض جديد</h3>
      <input name="full_name" placeholder="الاسم الكامل" value={formData.full_name} onChange={handleChange} />
      <input name="birth_date" type="date" value={formData.birth_date} onChange={handleChange} />
      <select name="gender" value={formData.gender} onChange={handleChange}>
        <option value="">اختر الجنس</option>
        <option value="ذكر">ذكر</option>
        <option value="أنثى">أنثى</option>
      </select>
      <button type="submit">إضافة</button>
    </form>
  );
}

export default AddPatientForm;
