import './Form.css';

function Form(){
    return(
            <form id='form'>
                <select className='dropdown' name='role'>
                    <option value='' disabled selected>Select a Role</option>
                    <option value='admin'>Admin</option>
                    <option value='faculty'>Faculty</option>
                    <option value='student'>Student</option>
                </select>
                <input type='text' className='textbox' name='ID'/> 
                <button className='submit' type='submit'>Submit</button>
            </form>
    );
}

export default Form;