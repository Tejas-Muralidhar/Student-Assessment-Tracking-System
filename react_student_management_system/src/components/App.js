import './App.css';
import Header from './Header';
import Form from './Form';

function App() {
  return (
    <div className="App">
      <Header />
      <hr style={{margin: 0}}/>
      <h1 id='title'>Student Marks and Attendance Monitoring System</h1>
      <Form />
      <button id='help'>Help</button>
    </div>
  );
}

export default App;
