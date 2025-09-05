from src.package_name.main import main


def test_main(capfd):
	main()
	out, err = capfd.readouterr()
	assert out == 'Hello from my package!\n'
