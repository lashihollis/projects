import express from 'express';
import cors from 'cors';
import appointmentsRouter from './routes/appointments'; 

const app = express();
app.use(cors());
app.use(express.json());

app.get('/', (_req, res) => {
  res.send('Welcome to CareSync API');
});

app.use('/appointments', appointmentsRouter);

app.listen(3001, () => {
  console.log('Server is running on http://localhost:3001');
});
