import { useState } from 'react';
import { createAppointment } from '../api/appointments';

export default function BookAppointmentForm() {
  const [form, setForm] = useState({ name: '', date: '', reason: '' });

  const handleChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    setForm({ ...form, [e.target.name]: e.target.value });
  };

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    await createAppointment(form);
    alert('Appointment booked!');
    setForm({ name: '', date: '', reason: '' });
  };

  return (
    <form onSubmit={handleSubmit}>
      <input name="name" placeholder="Name" value={form.name} onChange={handleChange} />
      <input name="date" type="date" value={form.date} onChange={handleChange} />
      <input name="reason" placeholder="Reason" value={form.reason} onChange={handleChange} />
      <button type="submit">Book Appointment</button>
    </form>
  );
}
