#!/usr/bin/python3

# Security conference abbreviations
# booktitle: AsiaCCS
# booktitle: CCS
# booktitle: CODASPY
# booktitle: WOOT
# booktitle: USENIX Security Symposium
# booktitle: NDSS
# booktitle: EuroS&amp;P
# booktitle: USENIX Annual Technical Conference
# booktitle: RTSS
# booktitle: DIMVA
# booktitle: OSDI
# booktitle: ESORICS
# booktitle: IEEE Symposium on Security and Privacy

# check out https://github.com/emeryberger/CSrankings/blob/gh-pages/filter.xq for conference names

CONFERENCES = {
    'sys_arch': ['ASPLOS', 'ISCA', 'MICRO', 'HPCA'],
    'sys_net': ['SIGCOMM', 'NSDI'],
    'sys_sec': ['CCS', 'ACM Conference on Computer and Communications Security', 'USENIX Security', 'USENIX Security Symposium', 'NDSS', 'IEEE Symposium on Security and Privacy'],
    #'sys_db': ['SIGMOD Conference', 'VLDB', 'PVLDB', 'Proc. VLDB Endow.', 'ICDE', 'PODS'],
    'sys_db': ['SIGMOD Conference', 'VLDB', 'PVLDB', 'Proc. VLDB Endow.'],
    #加上tdsc tifs
    'sec_withjournal': ['CCS', 'ACM Conference on Computer and Communications Security', 'USENIX Security', 'USENIX Security Symposium', 'NDSS', 'IEEE Symposium on Security and Privacy'] + ['IEEE Trans. Dependable Secur. Comput.', 'IEEE Trans. Inf. Forensics Secur.'],
    'sys_design': ['DAC', 'ICCAD'],
    'sys_embed': ['EMSOFT', 'RTAS', 'RTSS'],
    'sys_hpc': ['HPDC', 'ICS', 'SC'],
    'sys_mob': ['MobiSys', 'MobiCom', 'MOBICOM', 'SenSys'],
    'sys_mes': ['IMC', 'Internet Measurement Conference', 'Proc. ACM Meas. Anal. Comput. Syst.'],
    'sys_os': ['SOSP', 'OSDI', 'EuroSys', 'USENIX Annual Technical Conference', 'USENIX Annual Technical Conference, General Track', 'FAST'],
    'sys_pl': ['PLDI', 'POPL', 'ICFP', 'OOPSLA', 'OOPSLA/ECOOP'],
    #'sys_se': ['SIGSOFT FSE', 'ESEC/SIGSOFT FSE', 'ICSE', 'ICSE (1)', 'ICSE (2)', 'ASE', 'ISSTA'],
    'sys_se': ['SIGSOFT FSE', 'ESEC/SIGSOFT FSE', 'ICSE', 'ICSE (1)', 'ICSE (2)'],
    'ccfa':['ACM Trans. Comput. Syst.', 'ACM Trans. Storage', 'IEEE Trans. Comput. Aided Des. Integr. Circuits Syst.', 'IEEE Trans. Computers', 'IEEE Trans. Parallel Distributed Syst.', 'ACM Trans. Archit. Code Optim.', 'PPoPP', 'FAST', 'DAC', 'HPCA', 'MICRO', 'SC', 'ASPLOS', 'ISCA', 'USENIX Annual Technical Conference', 'USENIX Annual Technical Conference, General Track', 'EuroSys', 'IEEE J. Sel. Areas Commun.', 'IEEE Trans. Mob. Comput.', 'IEEE/ACM Trans. Netw.', 'SIGCOMM', 'MobiCom', 'MOBICOM', 'INFOCOM', 'NSDI', 'IEEE Trans. Dependable Secur. Comput.', 'IEEE Trans. Inf. Forensics Secur.', 'J. Cryptol.', 'CCS', 'ACM Conference on Computer and Communications Security', 'EUROCRYPT', 'IEEE Symposium on Security and Privacy', 'CRYPTO', 'USENIX Security Symposium', 'USENIX Security', 'NDSS', 'ACM Trans. Program. Lang. Syst.', 'ACM Trans. Softw. Eng. Methodol.', 'IEEE Trans. Software Eng.', 'IEEE Trans. Serv. Comput.', 'PLDI', 'POPL', 'ESEC/SIGSOFT FSE', 'SIGSOFT FSE', 'SOSP', 'OOPSLA', 'OOPSLA/ECOOP', 'ASE', 'ICSE', 'ICSE (1)', 'ICSE (2)', 'ISSTA', 'OSDI', 'FM', 'ACM Trans. Database Syst.', 'ACM Trans. Inf. Syst.', 'IEEE Trans. Knowl. Data Eng.', 'VLDB J.', 'SIGMOD Conference', 'KDD', 'ICDE', 'SIGIR', 'Proc. VLDB Endow.', 'VLDB', 'PVLDB', 'IEEE Trans. Inf. Theory', 'Inf. Comput.', 'SIAM J. Comput.', 'STOC', 'SODA', 'CAV', 'FOCS', 'LICS', 'ACM Trans. Graph.', 'IEEE Trans. Image Process.', 'IEEE Trans. Vis. Comput. Graph.', 'ACM Multimedia', 'SIGGRAPH', 'VR', 'IEEE Trans. Vis. Comput. Graph.', 'IEEE VIS', 'Artif. Intell.', 'IEEE Trans. Pattern Anal. Mach. Intell.', 'Int. J. Comput. Vis.', 'J. Mach. Learn. Res.', 'AAAI', 'NeurIPS', 'ACL', 'CVPR', 'ICCV', 'ICML', 'IJCAI', 'ACM Trans. Comput. Hum. Interact.', 'Int. J. Hum. Comput. Stud.', 'Proc. ACM Hum. Comput. Interact.', 'CHI', 'ISWC', 'UIST', 'J. ACM', 'Proc. IEEE', 'Sci. China Inf. Sci.', 'WWW', 'RTSS', 'WINE'],
    "tsinghuaa":['ACM Trans. Comput. Syst.', 'ACM Trans. Storage', 'IEEE Trans. Comput. Aided Des. Integr. Circuits Syst.', 'IEEE Trans. Computers', 'IEEE Trans. Parallel Distributed Syst.', 'ICSA', 'FAST', 'ASPLOS', 'EuroSys', 'HPCA', 'SIGMETRICS', 'FPGA', 'USENIX Annual Technical Conference', 'USENIX Annual Technical Conference, General Track', 'MICRO', 'SC', 'PPoPP', 'DAC', 'IEEE J. Sel. Areas Commun.', 'IEEE Trans. Mob. Comput.', 'IEEE/ACM Trans. Netw.', 'IEEE Trans. Commun.', 'SIGCOMM', 'NSDI', 'MobiCom', 'MOBICOM', 'MobiSys', 'IMC', 'Internet Measurement Conference', 'IPSN', 'SenSys', 'INFOCOM', 'CoNEXT', 'ICNP', 'IEEE Trans. Inf. Forensics Secur.', 'J. Cryptol.', 'IEEE Trans. Dependable Secur. Comput.', 'IEEE Symposium on Security and Privacy', 'NDSS', 'USENIX Security Symposium', 'USENIX Security', 'CCS', 'ACM Conference on Computer and Communications Security', 'EUROCRYPT', 'CRYPTO', 'CHES', 'ASIACRYPT', 'SIAM J. Comput.', 'IEEE Trans. Inf. Theory', 'ACM Trans. Algorithms', 'Inf. Comput.', 'STOC', 'FOCS', 'SODA', 'CAV', 'LICS', 'CCC', 'ICALP', 'IEEE Trans. Software Eng.', 'ACM Trans. Softw. Eng. Methodol.', 'ACM Trans. Program. Lang. Syst.', 'OSDI', 'ICSE', 'ICSE (1)', 'ICSE (2)', 'SOSP', 'POPL', 'PLDI', 'ESEC/SIGSOFT FSE', 'SIGSOFT FSE', 'ISSTA', 'OOPSLA', 'OOPSLA/ECOOP', 'ASE', 'IEEE Trans. Knowl. Data Eng.', 'VLDB J.', 'ACM Trans. Database Syst.', 'ACM Trans. Inf. Syst.', 'SIGMOD Conference', 'KDD', 'SIGIR', 'WSDM', 'Proc. VLDB Endow.', 'VLDB', 'PVLDB', 'ICDE', 'PODS', 'IEEE Trans. Pattern Anal. Mach. Intell.', 'Int. J. Comput. Vis.', 'J. Mach. Learn. Res.', 'IEEE Trans. Robotics', 'Artif. Intell.', 'IEEE ACM Trans. Audio Speech Lang. Process.', 'CVPR', 'ICCV', 'ICML', 'ACL', 'ECCV', 'COLT', 'NeurIPS', 'AAAI', 'EMNLP', 'ICRA', 'ICLR', 'Robotics - Science and Systems', 'IEEE Trans. Image Process.', 'ACM Trans. Graph.', 'IEEE Trans. Multim.', 'IEEE Trans. Vis. Comput. Graph.', 'Comput. Aided Des.', 'SIGGRAPH', 'IEEE Trans. Vis. Comput. Graph.', 'IEEE VIS', 'ACM Multimedia', 'VR', 'Int. J. Hum. Comput. Stud.', 'ACM Trans. Comput. Hum. Interact.', 'Proc. ACM Hum. Comput. Interact.', 'ISWC', 'UIST', 'CHI', 'J. ACM', 'Proc. IEEE', 'Sci. China Inf. Sci.', 'RECOMB', 'ISMB', 'WWW', 'EC'],
}

CONFERENCES_NUMBER = {
    'sys_arch': {},
    'sys_net': {},
    'sys_sec': {},
    'sys_db': {},
    'sys_design': {},
    'sys_embed': {},
    'sys_hpc': {},
    'sys_mob': {},
    'sys_mes': {},
    'sys_os': {},
    'sys_pl': {'Proc. ACM Program. Lang.' : ['POPL', 'OOPSLA', 'ICFP']},
    'sys_se': {},
    'sec_withjournal':{},
    'ccfa':{},
    "tsinghuaa":{},
}

CONFERENCES_SHORT = {
    'sys_arch': ['ASPLOS', 'ISCA', 'MICRO', 'HPCA'],
    'sys_net': ['SIGCOMM', 'NSDI'],
    'sys_sec': ['CCS', 'USENIX Security', 'NDSS', 'Oakland'],
    #'sys_db': ['SIGMOD', 'VLDB', 'ICDE', 'PODS'],
    'sys_db': ['SIGMOD', 'VLDB'],
    'sys_design': ['DAC', 'ICCAD'],
    'sys_embed': ['EMSOFT', 'RTAS', 'RTSS'],
    'sys_hpc': ['HPDC', 'ICS', 'SC'],
    'sys_mob': ['MobiSys', 'MobiCom', 'SenSys'],
    'sys_mes': ['IMC', 'SIGMETRICS'],
    'sys_os': ['SOSP', 'OSDI', 'EuroSys', 'USENIX ATC', 'FAST'],
    'sys_pl': ['PLDI', 'POPL', 'ICFP', 'OOPSLA'],
    #'sys_se': ['FSE', 'ICSE', 'ASE', 'ISSTA'],
    'sys_se': ['FSE', 'ICSE'],
    'sec_withjournal':['CCS', 'USENIX Security', 'NDSS', 'Oakland', "TDSC", "TIFS"],
    'ccfa':["CCF A类"],
    "tsinghuaa":["清华 A类"],
}

AREA_TITLES = {
    'sys_arch': 'Systems: Architecture',
    'sys_net': 'Systems: Networks',
    'sys_sec': 'Systems: Security',
    'sys_db': 'Systems: Databases',
    'sys_design': 'Systems: Design',
    'sys_embed': 'Embedded Systems',
    'sys_hpc': 'Systems: HPC',
    'sys_mob': 'Mobile Systems',
    'sys_mes': 'Systems: Measurements',
    'sys_os': 'Systems: OS',
    'sys_pl': 'Systems: Programming Languages',
    'sys_se': 'Systems: Software Engineering',
    'sys': 'All Areas',
    'sec_withjournal':'Systems: Security (with journal)',
    'ccfa':"CCF A类",
    "tsinghuaa":"清华 A类",
}

class Pub():
    def __init__(self, venue, title, authors, year):
        self.venue = venue
        self.title = title
        self.authors = authors
        self.year = year
        #print('{} {} {} {}\n'.format(authors, year, venue, title))

class Author():
    def __init__(self, name, aux_data):
        self.name = name
        self.years = {}
        self.nr_authors_year = {}
        self.venues = []
        self.normalized_pubs = {}
        self.affiliation, self.homepage, self.scholar = aux_data

    def add_norm_area(self, year, fraction):
        if not year in self.normalized_pubs:
            self.normalized_pubs[year] = 0
        self.normalized_pubs[year] += fraction

    def add_publication(self, venue, year, title, authors):
        if not year in self.years:
            self.years[year] = 0
            self.nr_authors_year[year] = []
        self.years[year] += 1
        self.nr_authors_year[year].append(len(authors))

        if not venue in self.venues:
            self.venues.append(venue)

    def get_total(self):
        return sum(self.years.values())

if __name__ == '__main__':
    print('Nothing to see here, move along...')
