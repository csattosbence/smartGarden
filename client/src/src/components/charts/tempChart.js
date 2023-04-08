import {
    Line,
    LineChart,
    XAxis,
    YAxis,
    CartesianGrid,
    ResponsiveContainer,
    Tooltip,
    Legend
  } from 'recharts';



const TempChart = ({data}) =>{
    return(
        
        <div className='temp-chart'>
            <ResponsiveContainer width="80%" height={200}>
            <LineChart  data={data}>
                <XAxis dataKey="currentDate"/>
                <YAxis dataKey="temperature"/>
                <Tooltip/>
                <Legend verticalAlign="top" height={36}/>
                <Line name="Temperature °C" type="monotone" dataKey="temperature" stroke="#f73636" />
                <CartesianGrid strokeDasharray="3 3" />
            </LineChart>
            </ResponsiveContainer>
        </div>
    )
}

export default TempChart;