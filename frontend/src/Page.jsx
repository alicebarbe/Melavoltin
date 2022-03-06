import React, {useState, useEffect} from 'react';
import * as styles from './styles';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome'
import { faBoltLightning } from '@fortawesome/free-solid-svg-icons';
import {useData} from './DataContext';
import { collection, getDocs } from 'firebase/firestore/lite';
import { ref, set, onValue, update, get } from 'firebase/database';
import { LineChart, Line, XAxis, YAxis, Label, ResponsiveContainer, CartesianGrid, Tooltip } from 'recharts';
import { fromUnixTime, format } from 'date-fns';


const Page = () =>{

  const [time, setTime] = useState('');
  const [data, setData] = useState([]);
  const {db} = useData();
  const {rtdb} = useData();

  const getData = async () => {
    const sleepCol = collection(db, 'biometric_data');
    const sleepSnapshot = await getDocs(sleepCol);
    const sleepList = sleepSnapshot.docs.map(doc => doc.data());
    console.log(sleepList);
    setData(sleepList);
  };

  useEffect( () => {
    setTime(localStorage.getItem('wakeupTime'));
    getData();
  }, [])

  const onChange = (event) => {
    setTime(event.target.value)
  };

  //get current and return the new
  //update using new
  
  const updateSleep = () => {
    onValue(ref(rtdb, 'SleepOn/'), (snapshot) => {
      const state =  snapshot.val().SleepyTime; 
      const newState = (state == 1) ? 0 : 1;
      update(ref(rtdb, 'SleepOn/'), {
        SleepyTime: newState
      })
    }, {onlyOnce: true});
  };

  const onClick = () => {
    updateSleep();
  }



  useEffect( () => {
    localStorage.setItem('wakeupTime', time)
    // let intTime = parseInt(time.replace(':',''));
    set(ref(rtdb, 'Control/'),{
      wakeup: time.replace(':','')
    });
  }, [time])


  return <>
      <styles.Container>

      <styles.Text size="1.5rem"><b>melavoltin </b><FontAwesomeIcon icon={faBoltLightning}/></styles.Text>

      <styles.TimeInput type="time" step="60" value={time} name="time" id="name" onChange={onChange}/>
      
        <styles.Text>Wake-up set for {time}</styles.Text>
    
        <styles.Ready onClick={onClick}>Ready for bed</styles.Ready>
        <styles.Text>TENS relaxation will begin as soon as you press the ready button.</styles.Text>


        <styles.Divider/>


        <styles.Text size="1.5rem"><b>Sleep Stats</b></styles.Text>

        <ResponsiveContainer width={"100%"} height={400}>
          <LineChart width={400} height={300} data={data} margin={{ top: 30, right: 30, left: 30, bottom: 30 }} stroke="#adc8cb">
            <CartesianGrid />
            <XAxis dataKey="timestamp" domain={["dataMin", "dataMax"]} stroke="#adc8cb">
              <Label value={"Time"} position="bottom" style={{ textAnchor: "middle" }}/>
            </XAxis>
          
            <YAxis stroke="#adc8cb">
              <Label value={"Heart Rate"} position="left" angle={-90} style={{ textAnchor: "middle" }}/>
            </YAxis>
            <Tooltip  />
            <Line dataKey="hr" name="Heart Rate" stroke="#adc8cb" dot={true} isAnimationActive={false}/>
          </LineChart>
        </ResponsiveContainer>

      </styles.Container>
  </>
}

export default Page;
