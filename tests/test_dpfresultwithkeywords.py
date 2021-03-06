import os
from ansys import dpf
from ansys.dpf import post
from ansys.dpf.core.common import locations
import numpy as np
import unittest
import pytest
    
    
def test_displacement_with_scoping_verbose_api(allkindofcomplexity):
    result = post.load_solution(allkindofcomplexity)
    #scoping as array
    disp = result.misc.nodal_displacement(node_scoping = [1, 2])
    data = disp.get_data_at_field(0)
    assert len(data) == 2
    assert len(data[0]) == 3
    #scoping as dpf.Scoping
    scop = dpf.core.Scoping()
    scop.ids = [1, 2]
    scop.location = locations.nodal
    disp2 = result.misc.nodal_displacement(node_scoping = scop)
    data2 = disp2.get_data_at_field(0)
    assert len(data2) == 2
    assert len(data2[0]) == 3
    #scoping as int
    disp3 = result.misc.nodal_displacement(node_scoping = 1)
    data3 = disp3.get_data_at_field(0)
    assert len(data3) == 1
    assert len(data3[0]) == 3
    #values comparison
    assert np.allclose(data, data2)
    

def test_displacement_with_scoping(allkindofcomplexity):
    result = post.load_solution(allkindofcomplexity)
    #scoping as array
    disp = result.displacement(node_scoping = [1, 2])
    data = disp.vector.get_data_at_field(0)
    assert len(data) == 2
    assert len(data[0]) == 3
    #scoping as dpf.Scoping
    scop = dpf.core.Scoping()
    scop.ids = [1, 2]
    scop.location = locations.nodal
    disp2 = result.displacement(node_scoping = scop)
    data2 = disp2.vector.get_data_at_field(0)
    assert len(data2) == 2
    assert len(data2[0]) == 3
    #scoping as int
    disp3 = result.displacement(node_scoping = 1)
    data3 = disp3.vector.get_data_at_field(0)
    assert len(data3) == 1
    assert len(data3[0]) == 3
    #values comparison
    assert np.allclose(data, data2)
            

def test_node_stress_with_scoping_verbose_api(allkindofcomplexity):
    result = post.load_solution(allkindofcomplexity)
    #scoping as array
    disp = result.misc.nodal_stress(element_scoping = [1, 34])
    data = disp.get_data_at_field(0)
    assert len(data) == 40
    assert len(data[0]) == 6
    #scoping as dpf.Scoping
    scop = dpf.core.Scoping()
    scop.location = locations.elemental
    scop.ids = [1, 34]
    disp2 = result.misc.nodal_stress(element_scoping = scop)
    data2 = disp2.get_data_at_field(0)
    assert len(data2) == 40
    assert len(data2[0]) == 6
    #scoping as int
    disp3 = result.misc.nodal_stress(element_scoping = 1)
    data3 = disp3.get_data_at_field(0)
    assert len(data3) == 20
    assert len(data3[0]) == 6
    #values comparison
    assert np.allclose(data, data2)
    

def test_node_stress_with_scoping(allkindofcomplexity):
    result = post.load_solution(allkindofcomplexity)
    #scoping as array
    disp = result.stress(element_scoping = [1, 34])
    data = disp.tensor.get_data_at_field(0)
    assert len(data) == 40
    assert len(data[0]) == 6
    #scoping as dpf.Scoping
    scop = dpf.core.Scoping()
    scop.location = locations.elemental
    scop.ids = [1, 34]
    disp2 = result.stress(element_scoping = scop)
    data2 = disp2.tensor.get_data_at_field(0)
    assert len(data2) == 40
    assert len(data2[0]) == 6
    #scoping as int
    disp3 = result.stress(element_scoping = 1)
    data3 = disp3.tensor.get_data_at_field(0)
    assert len(data3) == 20
    assert len(data3[0]) == 6
    #values comparison
    assert np.allclose(data, data2)
    
    
def test_elemnodal_stress_with_scoping_verbose_api(allkindofcomplexity):
    result = post.load_solution(allkindofcomplexity)
    #scoping as array
    disp = result.misc.elemental_nodal_stress(element_scoping = [1, 34])
    data = disp.get_data_at_field(0)
    assert len(data) == 16
    assert len(data[0]) == 6
    #scoping as dpf.Scoping
    scop = dpf.core.Scoping()
    scop.location = locations.elemental
    scop.ids = [1, 34]
    disp2 = result.misc.elemental_nodal_stress(element_scoping = scop)
    data2 = disp2.get_data_at_field(0)
    assert len(data2) == 16
    assert len(data2[0]) == 6
    #scoping as int
    disp3 = result.misc.elemental_nodal_stress(element_scoping = 1)
    data3 = disp3.get_data_at_field(0)
    assert len(data3) == 8
    assert len(data3[0]) == 6
    #values comparison
    assert np.allclose(data, data2)
    

def test_elemnodal_stress_with_scoping(allkindofcomplexity):
    result = post.load_solution(allkindofcomplexity)
    #scoping as array
    disp = result.stress(element_scoping = [1, 34], location=post.locations.elemental_nodal)
    data = disp.tensor.get_data_at_field(0)
    assert len(data) == 16
    assert len(data[0]) == 6
    #scoping as dpf.Scoping
    scop = dpf.core.Scoping()
    scop.location = locations.elemental
    scop.ids = [1, 34]
    disp2 = result.stress(element_scoping = scop, location=post.locations.elemental_nodal)
    data2 = disp2.tensor.get_data_at_field(0)
    assert len(data2) == 16
    assert len(data2[0]) == 6
    #scoping as int
    disp3 = result.stress(element_scoping = 1, location=post.locations.elemental_nodal)
    data3 = disp3.tensor.get_data_at_field(0)
    assert len(data3) == 8
    assert len(data3[0]) == 6
    #values comparison
    assert np.allclose(data, data2)
    
    
def test_disp_with_component_subresult_verbose_api(allkindofcomplexity):
    result = post.load_solution(allkindofcomplexity)
    disp = result.misc.nodal_displacement(subresult="Y")
    assert disp._evaluator._result_operator.name == "UY"
    assert disp.num_fields == 1
    data = disp.get_data_at_field(0)
    assert len(data) == 15113
    assert np.isclose(data[0], 5.130250313479703e-06)

    
def test_disp_with_component_subresult(allkindofcomplexity):
    result = post.load_solution(allkindofcomplexity)
    d = result.displacement()
    disp = d.y
    assert disp._evaluator._result_operator.name == "UY"
    assert disp.num_fields == 1
    data = disp.get_data_at_field(0)
    assert len(data) == 15113
    assert np.isclose(data[0], 5.130250313479703e-06)


def test_stress_with_component_subresult_verbose_api(allkindofcomplexity):
    result = post.load_solution(allkindofcomplexity)
    stress = result.misc.elemental_nodal_stress(subresult="YZ")
    assert stress._evaluator._result_operator.name == "SYZ"
    assert stress.num_fields == 1
    data = stress.get_data_at_field(0)
    assert len(data) == 40016
    assert np.isclose(data[1], 1.0216815465593042e-10)
    
    
def test_stress_with_component_subresult(allkindofcomplexity):
    result = post.load_solution(allkindofcomplexity)
    s = result.stress(location=post.locations.elemental_nodal)
    stress = s.yz
    assert stress._evaluator._result_operator.name == "SYZ"
    assert stress.num_fields == 1
    data = stress.get_data_at_field(0)
    assert len(data) == 40016
    assert np.isclose(data[1], 1.0216815465593042e-10)


def test_stress_with_invariant_subresult_verbose_api(allkindofcomplexity):
    result = post.load_solution(allkindofcomplexity)
    stress = result.misc.elemental_nodal_stress(subresult="3")
    assert stress._evaluator._result_operator.name == "S3"
    assert stress.num_fields == 2
    data = stress.get_data_at_field(0)
    assert len(data) == 720
    assert np.isclose(data[1], -4721842.179373354)
    

def test_stress_with_invariant_subresult(allkindofcomplexity):
    result = post.load_solution(allkindofcomplexity)
    s = result.stress(location=post.locations.elemental_nodal)
    stress = s.principal_3
    assert stress._evaluator._result_operator.name == "S3"
    assert stress.num_fields == 2
    data = stress.get_data_at_field(0)
    assert len(data) == 720
    assert np.isclose(data[1], -4721842.179373354)
    
    
def test_groupingelshape_nodallocation_verbose_api(allkindofcomplexity):
    result = post.load_solution(allkindofcomplexity)
    disp = result.misc.nodal_displacement(grouping = post.grouping.by_el_shape)
    assert disp.num_fields == 4
    assert disp.result_fields_container.get_label_space(3) == {'elshape': 3, 'time': 1}
    assert len(disp.get_data_at_field(0)) == 93950
    assert len(disp.get_data_at_field(1)) == 6748
    assert len(disp.get_data_at_field(2)) == 36
    assert len(disp.get_data_at_field(3)) == 4
    assert np.isclose(disp.get_data_at_field(2)[0][0], 5.523488975819807e-20)
    assert disp[0].location == locations.nodal
    
    
def test_groupingelshape_nodallocation(allkindofcomplexity):
    result = post.load_solution(allkindofcomplexity)
    d = result.displacement(grouping = post.grouping.by_el_shape)
    disp = d.vector
    assert disp.num_fields == 4
    assert disp.result_fields_container.get_label_space(3) == {'elshape': 3, 'time': 1}
    assert len(disp.get_data_at_field(0)) == 93950
    assert len(disp.get_data_at_field(1)) == 6748
    assert len(disp.get_data_at_field(2)) == 36
    assert len(disp.get_data_at_field(3)) == 4
    assert np.isclose(disp.get_data_at_field(2)[0][0], 5.523488975819807e-20)
    assert disp[0].location == locations.nodal


def test_groupingelshape_elemlocation_verbose_api(allkindofcomplexity):
    result = post.load_solution(allkindofcomplexity)
    stress = result.misc.elemental_stress(grouping = post.grouping.by_el_shape)
    assert stress.num_fields == 4
    assert stress.result_fields_container.get_label_space(3) == {'elshape': 3, 'time': 1}
    assert len(stress.get_data_at_field(0)) == 609
    assert len(stress.get_data_at_field(1)) == 27156
    assert len(stress.get_data_at_field(2)) == 0
    assert len(stress.get_data_at_field(3)) == 0
    assert np.isclose(stress.get_data_at_field(1)[0][0], -2984789.100540372)
    assert stress[0].location == locations.elemental
    
    
def test_groupingelshape_elemlocation(allkindofcomplexity):
    result = post.load_solution(allkindofcomplexity)
    s = result.stress(grouping = post.grouping.by_el_shape, location=post.locations.elemental)
    stress = s.tensor
    assert stress.num_fields == 4
    assert stress.result_fields_container.get_label_space(3) == {'elshape': 3, 'time': 1}
    assert len(stress.get_data_at_field(0)) == 609
    assert len(stress.get_data_at_field(1)) == 27156
    assert len(stress.get_data_at_field(2)) == 0
    assert len(stress.get_data_at_field(3)) == 0
    assert np.isclose(stress.get_data_at_field(1)[0][0], -2984789.100540372)
    assert stress[0].location == locations.elemental
    

def test_groupingmat_nodallocation_verbose_api(allkindofcomplexity):
    result = post.load_solution(allkindofcomplexity)
    disp = result.misc.nodal_displacement(grouping = post.grouping.by_material)
    assert disp.num_fields == 11
    assert len(disp[0]) == 23016
    assert len(disp[2]) == 1848
    assert np.isclose(disp.get_data_at_field(2)[0][2], -6.649053654123576e-07)
    assert disp.result_fields_container.get_label_space(3) == {'time': 1, 'mat': 10}
    
    
def test_groupingmat_nodallocation(allkindofcomplexity):
    result = post.load_solution(allkindofcomplexity)
    d = result.displacement(grouping = post.grouping.by_material)
    disp = d.vector
    assert disp.num_fields == 11
    assert len(disp[0]) == 23016
    assert len(disp[2]) == 1848
    assert np.isclose(disp.get_data_at_field(2)[0][2], -6.649053654123576e-07)
    assert disp.result_fields_container.get_label_space(3) == {'time': 1, 'mat': 10}
    

def test_groupingmat_elemlocation_verbose_api(allkindofcomplexity):
    result = post.load_solution(allkindofcomplexity)
    stress = result.misc.elemental_stress(grouping = post.grouping.by_material)
    assert stress.num_fields == 11
    assert len(stress[1]) == 9828
    assert len(stress[5]) == 156762
    assert stress.get_data_at_field(5)[0][2] == 2255995657.8043337
    assert stress.result_fields_container.get_label_space(3) == {'time': 1, 'mat': 4}
    assert stress[1].location == locations.elemental
    

def test_groupingmat_elemlocation(allkindofcomplexity):
    result = post.load_solution(allkindofcomplexity)
    s = result.stress(grouping = post.grouping.by_material, location=post.locations.elemental)
    stress = s.tensor
    assert stress.num_fields == 11
    assert len(stress[1]) == 9828
    assert len(stress[5]) == 156762
    assert stress.get_data_at_field(5)[0][2] == 2255995657.8043337
    assert stress.result_fields_container.get_label_space(3) == {'time': 1, 'mat': 4}
    assert stress[1].location == locations.elemental
    

def test_mapdlgrouping_nodallocation_verbose_api(allkindofcomplexity):
    result = post.load_solution(allkindofcomplexity)
    disp = result.misc.nodal_displacement(mapdl_grouping = 186)
    try:
        disp.num_fields
    except:
        assert True
        
        
def test_mapdlgrouping_nodallocation(allkindofcomplexity):
    result = post.load_solution(allkindofcomplexity)
    d = result.displacement(mapdl_grouping = 186)
    disp = d.vector
    try:
        disp.num_fields
    except:
        assert True
    

def test_maplgrouping_elemlocation_verbose_api(allkindofcomplexity):
    result = post.load_solution(allkindofcomplexity)
    stress = result.misc.elemental_stress(mapdl_grouping = 186)
    assert stress.num_fields == 1
    assert stress.result_fields_container.get_label_space(0) == {'time': 1}
    assert len(stress.get_data_at_field(0)) == 343
    assert np.isclose(stress.get_data_at_field(0)[41][2], -323198.184976747)
    assert stress[0].location == locations.elemental
    
    
def test_maplgrouping_elemlocation(allkindofcomplexity):
    result = post.load_solution(allkindofcomplexity)
    s = result.stress(mapdl_grouping = 186, location=post.locations.elemental)
    stress = s.tensor
    assert stress.num_fields == 1
    assert stress.result_fields_container.get_label_space(0) == {'time': 1}
    assert len(stress.get_data_at_field(0)) == 343
    assert np.isclose(stress.get_data_at_field(0)[41][2], -323198.184976747)
    assert stress[0].location == locations.elemental
    

def test_set_keyword_verbose_api(plate_msup):
    result = post.load_solution(plate_msup)
    disp = result.misc.nodal_displacement(set = 3)
    assert disp.num_fields == 1
    assert disp.result_fields_container.get_label_space(0) == {'time': 3}
    assert np.isclose(disp.get_data_at_field(0)[2][2], 2.3955190605044603e-05)
    
    
def test_set_keyword(plate_msup):
    result = post.load_solution(plate_msup)
    d = result.displacement(set = 3)
    disp = d.vector
    assert disp.num_fields == 1
    assert disp.result_fields_container.get_label_space(0) == {'time': 3}
    assert np.isclose(disp.get_data_at_field(0)[2][2], 2.3955190605044603e-05)
    
    
class TestCase(unittest.TestCase):
    
    @pytest.fixture(autouse=True)
    def set_filepath(self, plate_msup):
        self._filepath = plate_msup
        
    def test_both_set_time_verbose_api(self):
        result = post.load_solution(self._filepath)
        self.assertRaises(Exception, result.misc.nodal_displacement, set=3, time=0.01)
        try:
            result.misc.nodal_displacement(set = 3, time = 0.01)
        except Exception as e:
            message = "Set, time and time_scoping keyword arguments must be used independently."
            e2 = Exception(message)
            assert e.args == e2.args
            assert type(e) == type(e2)
            

def test_time_keyword_in_frequencies_verbose_api(plate_msup):
    result = post.load_solution(plate_msup)
    disp = result.misc.nodal_displacement(time=0.06)
    assert disp.num_fields == 1
    assert disp.result_fields_container.get_label_space(0) == {'time': 6}
    assert np.isclose(disp.get_data_at_field(0)[2][2], 6.449354759605568e-05)
    disp = result.misc.nodal_displacement(time=0.02)
    assert disp.num_fields == 1
    assert disp.result_fields_container.get_label_space(0) == {'time': 2}
    assert np.isclose(disp.get_data_at_field(0)[40][2], -9.555678764252377e-06)
    disp = result.misc.nodal_displacement(time=0.14)
    assert disp.num_fields == 1
    assert disp.result_fields_container.get_label_space(0) == {'time': 14}
    assert np.isclose(disp.get_data_at_field(0)[22][2], -5.9753488295405e-06)
    disp = result.misc.nodal_displacement(time=0.15)
    assert disp.num_fields == 1
    assert disp.result_fields_container.get_label_space(0) == {'time': 15}
    assert np.isclose(disp.get_data_at_field(0)[101][2], 1.2454347438346573e-05)
    disp = result.misc.nodal_displacement(time=0.2)
    assert disp.num_fields == 1
    assert disp.result_fields_container.get_label_space(0) == {'time': 20}
    assert np.isclose(disp.get_data_at_field(0)[345][2], 6.931130871751968e-05)
    
    
def test_time_keyword_in_frequencies(plate_msup):
    result = post.load_solution(plate_msup)
    d = result.displacement(time=0.06)
    disp = d.vector
    assert disp.num_fields == 1
    assert disp.result_fields_container.get_label_space(0) == {'time': 6}
    assert np.isclose(disp.get_data_at_field(0)[2][2], 6.449354759605568e-05)
    d = result.displacement(time=0.02)
    disp = d.vector
    assert disp.num_fields == 1
    assert disp.result_fields_container.get_label_space(0) == {'time': 2}
    assert np.isclose(disp.get_data_at_field(0)[40][2], -9.555678764252377e-06)
    d = result.displacement(time=0.14)
    disp = d.vector
    assert disp.num_fields == 1
    assert disp.result_fields_container.get_label_space(0) == {'time': 14}
    assert np.isclose(disp.get_data_at_field(0)[22][2], -5.9753488295405e-06)
    d = result.displacement(time=0.15)
    disp = d.vector
    assert disp.num_fields == 1
    assert disp.result_fields_container.get_label_space(0) == {'time': 15}
    assert np.isclose(disp.get_data_at_field(0)[101][2], 1.2454347438346573e-05)
    d = result.displacement(time=0.2)
    disp = d.vector
    assert disp.num_fields == 1
    assert disp.result_fields_container.get_label_space(0) == {'time': 20}
    assert np.isclose(disp.get_data_at_field(0)[345][2], 6.931130871751968e-05)


def test_time_keyword_not_in_frequencies_verbose_api(plate_msup):
    result = post.load_solution(plate_msup)
    disp = result.misc.nodal_displacement(time=0.061)
    assert disp.num_fields == 1
    assert disp.result_fields_container.get_label_space(0) == {'time': 0}
    assert np.isclose(disp.get_data_at_field(0)[2][2], 6.466312449668174e-05)
    disp = result.misc.nodal_displacement(time=0.023)
    assert disp.num_fields == 1
    assert disp.result_fields_container.get_label_space(0) == {'time': 0}
    assert np.isclose(disp.get_data_at_field(0)[40][2], -1.3341949773184135e-05)
    disp = result.misc.nodal_displacement(time=0.1499)
    assert disp.num_fields == 1
    assert disp.result_fields_container.get_label_space(0) == {'time': 0}
    assert np.isclose(disp.get_data_at_field(0)[22][2], -1.7795334817918245e-05)
    
    
def test_time_keyword_not_in_frequencies(plate_msup):
    result = post.load_solution(plate_msup)
    d = result.displacement(time=0.061)
    disp = d.vector
    assert disp.num_fields == 1
    assert disp.result_fields_container.get_label_space(0) == {'time': 0}
    assert np.isclose(disp.get_data_at_field(0)[2][2], 6.466312449668174e-05)
    d = result.displacement(time=0.023)
    disp = d.vector
    assert disp.num_fields == 1
    assert disp.result_fields_container.get_label_space(0) == {'time': 0}
    assert np.isclose(disp.get_data_at_field(0)[40][2], -1.3341949773184135e-05)
    d = result.displacement(time=0.1499)
    disp = d.vector
    assert disp.num_fields == 1
    assert disp.result_fields_container.get_label_space(0) == {'time': 0}
    assert np.isclose(disp.get_data_at_field(0)[22][2], -1.7795334817918245e-05)
    
    
def test_time_scoping_keyword_verbose_api(plate_msup):
    result = post.load_solution(plate_msup)
    disp = result.misc.nodal_displacement()
    assert disp.num_fields == 1
    disp1 = result.misc.nodal_displacement(time_scoping=[1,2,4])
    assert disp1.num_fields == 3
    assert disp1.result_fields_container.get_label_space(0) == {'time': 1}
    assert np.isclose(disp1.get_data_at_field(0)[40][2], -2.0115581116044217e-06)
    # disp2 = result.misc.nodal_displacement(time_scoping=np.array([1, 2, 4]))
    # assert disp2.num_fields == 3
    # assert disp2.result_fields_container.get_label_space(0) == {'time': 1}
    # assert np.isclose(disp2.get_data_at_field(0)[40][2], -2.0115581116044217e-06)
    scop = dpf.core.Scoping()
    scop.ids = [1, 2, 4]
    disp3 = result.misc.nodal_displacement(time_scoping=scop)
    assert disp3.num_fields == 3
    assert disp3.result_fields_container.get_label_space(0) == {'time': 1}
    assert np.isclose(disp3.get_data_at_field(0)[40][2], -2.0115581116044217e-06)
    disp4 = result.misc.nodal_displacement(time_scoping=2)
    assert disp4.num_fields == 1
    assert disp4.result_fields_container.get_label_space(0) == {'time': 2}
    assert np.isclose(disp4.get_data_at_field(0)[40][2], -9.555678764252377e-06)
    
    
def test_time_scoping_keyword(plate_msup):
    result = post.load_solution(plate_msup)
    d = result.displacement()
    disp = d.vector
    assert disp.num_fields == 1
    d1 = result.displacement(time_scoping=[1,2,4])
    disp1 = d1.vector
    assert disp1.num_fields == 3
    assert disp1.result_fields_container.get_label_space(0) == {'time': 1}
    assert np.isclose(disp1.get_data_at_field(0)[40][2], -2.0115581116044217e-06)
    # disp2 = result.misc.nodal_displacement(time_scoping=np.array([1, 2, 4]))
    # assert disp2.num_fields == 3
    # assert disp2.result_fields_container.get_label_space(0) == {'time': 1}
    # assert np.isclose(disp2.get_data_at_field(0)[40][2], -2.0115581116044217e-06)
    scop = dpf.core.Scoping()
    scop.ids = [1, 2, 4]
    d3 = result.displacement(time_scoping=scop)
    disp3 = d3.vector
    assert disp3.num_fields == 3
    assert disp3.result_fields_container.get_label_space(0) == {'time': 1}
    assert np.isclose(disp3.get_data_at_field(0)[40][2], -2.0115581116044217e-06)
    d4 = result.displacement(time_scoping=2)
    disp4 = d4.vector
    assert disp4.num_fields == 1
    assert disp4.result_fields_container.get_label_space(0) == {'time': 2}
    assert np.isclose(disp4.get_data_at_field(0)[40][2], -9.555678764252377e-06)
    
    
def test_named_selection_keyword_verbose_api(model_ns):
    result = post.load_solution(model_ns)
    stress = result.misc.elemental_stress(named_selection="SELECTION")
    assert stress.num_fields == 1
    assert len(stress[0]) == 1260
    assert len(stress[0].data[20]) == 6
    assert np.isclose(stress.get_data_at_field(0)[40][2], -898513431744.8938)
    assert stress[0].location == post.locations.elemental
    
    
def test_named_selection_keyword(model_ns):
    result = post.load_solution(model_ns)
    s = result.stress(location=post.locations.elemental, named_selection="SELECTION")
    stress = s.tensor
    assert stress.num_fields == 1
    assert len(stress[0]) == 1260
    assert len(stress[0].data[20]) == 6
    assert np.isclose(stress.get_data_at_field(0)[40][2], -898513431744.8938)
    assert stress[0].location == post.locations.elemental
    
    
    