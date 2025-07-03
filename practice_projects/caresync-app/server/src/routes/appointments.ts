import express from 'express';

const router = express.Router();

type Appointment = {
  id: number;
  name: string;
  date: string;
  reason: string;
};

let appointments: Appointment[] = []; // in-memory mock database

// GET /appointments
router.get('/', (_req, res) => {
  res.json(appointments);
});

// POST /appointments
router.post('/', (req, res) => {
  const { name, date, reason } = req.body;
  const newAppointment = {
    id: Date.now(),
    name,
    date,
    reason,
  };
  appointments.push(newAppointment);
  res.status(201).json(newAppointment);
});

export default router;
