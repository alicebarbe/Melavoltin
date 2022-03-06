import React, { useContext, useState } from 'react';
import { initializeApp } from 'firebase/app';
import { getFirestore } from 'firebase/firestore/lite';
import { getDatabase } from 'firebase/database';


const DataContext = React.createContext();

const firebaseConfig = {
    apiKey: "AIzaSyCD7-h-8fpIZJUqNz_RddVG6bgg9F_BmkM",
    authDomain: "melavoltin.firebaseapp.com",
    databaseURL:"https://melavoltin-default-rtdb.europe-west1.firebasedatabase.app/",
    projectId: "melavoltin",
    storageBucket: "melavoltin.appspot.com",
    messagingSenderId: "93377483869",
    appId: "1:93377483869:web:678d8b475ad6ad9059e9b4"
  };


export const DataProvider = ({ children }) => {
    const app = initializeApp(firebaseConfig);
    const db = getFirestore(app);

    const rtdb = getDatabase();
    return <>
        <DataContext.Provider value={{app, db, rtdb}}>
            {children}
        </DataContext.Provider>
    </>
};

export const useData = () => useContext(DataContext);

export default DataContext;
