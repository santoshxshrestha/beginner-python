{
  description = "A Nix-flake-based python development environment";

  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs?ref=nixos-unstable";
  };

  outputs =
    { self, nixpkgs }:
    let
      system = "x86_64-linux";
      pkgs = import nixpkgs { inherit system; };
    in
    {
      devShells.${system}.default = pkgs.mkShell {
        buildInputs = with pkgs; [
          python3
          python3Packages.pip
          python3Packages.virtualenv
          python3Packages.setuptools
          python3Packages.wheel

          # Development tools
          python3Packages.black
          python3Packages.flake8
          python3Packages.mypy
          python3Packages.pytest
          python3Packages.isort

          # Language server
          python3Packages.python-lsp-server

          # Common Python packages
          python3Packages.requests
          python3Packages.numpy
          python3Packages.pandas
          python3Packages.django
          python3Packages.pillow
        ];

        shellHook = ''
          # Create virtual environment if it doesn't exist
          if [ ! -d ".venv" ]; then
            echo "Creating virtual environment..."
            python -m venv .venv
          fi

          # Activate virtual environment
          source .venv/bin/activate

          # Upgrade pip
          # pip install --upgrade pip
        '';
      };
    };
}
