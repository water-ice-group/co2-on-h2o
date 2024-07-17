#!/bin/bash
#SBATCH --job-name=XXXNAMEXXX
#SBATCH --time=24:00:00
#SBATCH --nodes=24
#SBATCH --tasks-per-node=128
#SBATCH --cpus-per-task=1
#SBATCH --account=XXXACCOUNTXXX
#SBATCH --partition=standard
#SBATCH --qos=standard

export SRUN_CPUS_PER_TASK=$SLURM_CPUS_PER_TASK
export OMP_NUM_THREADS=1

FILE=lammps
IPI=/path/to/ipi/executable
EXEC=/path/to/lammps/executable

module load cpe/22.12
module load cray-fftw/3.3.10.3
module load cmake/3.21.3
module load gsl/2.7
source /path/to/ipi/env.sh

if [ -e RESTART ]
then
	ipifile=RESTART
else 
	ipifile=input.xml
fi

hostname=$HOSTNAME
portnumber=11121

echo $SLURM_NODES
echo $SLURM_TASKS_PER_NODE
echo $SLURM_CPUS_PER_TASK
echo $OMP_NUM_THREADS

sed -i "s/address>.*</address>${hostname}</" ${ipifile}
sed -i "s/port>.*</port>${portnumber}</g" ${ipifile}
sed -i "s/ipi .* inet/ipi ${hostname} ${portnumber} inet/g" lammps.inp

${IPI} ${ipifile} > log.i-pi &
sleep 30

for i in {1..6}
do

srun --nodes=4 --ntasks=512 --distribution=block:block --hint=nomultithread ${EXEC} -i lammps.inp > log.lmp.${i} &

done

wait
