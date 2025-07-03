import BookAppointmentForm from './components/BookAppointmentForm';
import AppointmentList from './components/AppointmentList';

function App() {
  return (
    <div style={{ padding: '2rem' }}>
      <h1>CareSync</h1>
      <BookAppointmentForm />
      <hr />
      <AppointmentList />
    </div>
  );
}

export default App;
