from flow import FlowProject
import os

class Project(FlowProject):
    pass

##########################
# Labels
#########################

@Project.label
def chain_created(job):
    return job.isfile('start.data')

@Project.label
def simulation_complete(job):
    return job.isfile('final.data')


##########################
# Operations
#########################

@Project.post(chain_created)
@Project.operation(cmd=True, with_job=True)
def create_chain(job):

    chain_length           = job.sp.chain_length
    python_script_location = job.project.path + '/scripts/create_chain.py'

    command_to_run = f'python {python_script_location} {chain_length}'

    print(f'\nrunning create_chain.py on job id {job.id} to generate a chain with chain length = {chain_length}\n')

    return(command_to_run) 

@Project.pre(chain_created)
@Project.post(simulation_complete)
@Project.operation(cmd=True, with_job=True)
def run_simulation(job):

    lj_cutoff              = job.sp.lj_cutoff
    lammps_script_location = job.project.path + '/scripts/in.single_chain'

    command_to_run = f'srun lmp -screen out.lammps -in {lammps_script_location} -v lj_cutoff {lj_cutoff}'

    return(command_to_run)


if __name__=="__main__":
    Project().main()

