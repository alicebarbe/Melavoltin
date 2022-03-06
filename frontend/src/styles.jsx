import styled from 'styled-components';

export const Container = styled.div`
    display: flex;
    width:100%;
    max-width: 550px;
    color: #adc8cb;
    margin: 0 auto;
    justify-content: center;
    align-items: center;
    flex-direction: column;
`;

export const Text = styled.p`
    display: block;
    text-align: center;
    font-size: ${ props => props.size ? props.size : '1rem'};
`;

export const Ready = styled.button`
    display: block;
    border-radius:50px;
    padding: 1rem 2.5rem;
    border: none;
    font-size: 1.5rem;
    background-color:#adc8cb;
    color: #263132;
    font-family: Montserrat;
    margin-top: 2rem;
`;

export const Divider = styled.div`
    width: 100%;
    border-top: 1px solid #adc8cb;
    margin: 1rem 0;
`;



export const TimeInput = styled.input`
    background-color: #adc8cb;
    padding: 0.5rem 0.75rem;
    border: none;
    border-radius: 3px;
    font-size: 1.2rem;
    font-family: 'Montserrat';
    color:#263132;
`;