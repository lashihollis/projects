import { useEffect, useState } from 'react';
import { getAppointments } from '../api/appointments';

type Appointment = {
  id: number;
  name: string;
  date: string;
  reason: string;
};

export default function AppointmentList() {
  const [appointments, setAppointments] = useState<Appointment[]>([]);

  useEffect(() => {
    getAppointments().then(setAppointments);
  }, []);

  return (
    <div>
      <h2>Appointments</h2>
      <ul>
        {appointments.map((appt) => (
          <li key={appt.id}>
            {appt.name} - {appt.date} - {appt.reason}
          </li>
        ))}
      </ul>
    </div>
  );
}
