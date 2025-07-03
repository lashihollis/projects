const BASE_URL = 'http://localhost:3001/appointments';

export async function getAppointments() {
  const res = await fetch(BASE_URL);
  return res.json();
}

export async function createAppointment(data: {
  name: string;
  date: string;
  reason: string;
}) {
  const res = await fetch(BASE_URL, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(data),
  });
  return res.json();
}
