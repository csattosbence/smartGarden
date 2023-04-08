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



const HumidityChart = ({data}) =>{
    return(
        <ResponsiveContainer width="80%" height={200}>
        <LineChart  data={data}>
            <XAxis dataKey="currentDate"/>
            <YAxis dataKey="humidity"/>
            <Tooltip/>
            <Legend verticalAlign="top" height={36}/>
            <Line name="Humidity %" type="monotone" dataKey="humidity" stroke="#09b0e3" />
            <CartesianGrid strokeDasharray="3 3" />
        </LineChart>
        </ResponsiveContainer>
    )
}

export default HumidityChart;